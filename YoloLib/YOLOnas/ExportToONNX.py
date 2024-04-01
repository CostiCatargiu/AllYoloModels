from super_gradients.training import models
from super_gradients.common.object_names import Models


dataset_params = {
   'data_dir':'/home/constantin/Doctorat/FireDataset/DatasetAllTrainYOLOv8_shuffle',
   'train_images_dir':'train/images',
   'train_labels_dir':'train/labels',
   'val_images_dir':'valid/images',
   'val_labels_dir':'valid/labels',
   'test_images_dir':'test/images',
   'test_labels_dir':'test/labels',
   'classes': ['fire', 'other', 'smoke']
}

best_weights_path = '/home/constantin/Doctorat/YoloModels/YOLOnas/super-gradients/checkpoints/my_custom_yolonas_run/RUN_20240214_083607_689848/average_model.pth'
best_model = models.get('yolo_nas_s',
                        num_classes=len(dataset_params['classes']),
                        checkpoint_path=best_weights_path)


import torch
import torch.nn as nn

class TRT_NMS(torch.autograd.Function):
    '''TensorRT NMS operation'''
    @staticmethod
    def forward(
        ctx,
        boxes,
        scores,
        background_class=-1,
        box_coding=0,
        iou_threshold=0.45,
        max_output_boxes=100,
        plugin_version="1",
        score_activation=0,
        score_threshold=0.25,
    ):
        batch_size, num_boxes, num_classes = scores.shape
        num_det = torch.randint(0, max_output_boxes, (batch_size, 1), dtype=torch.int32)
        det_boxes = torch.randn(batch_size, max_output_boxes, 4)
        det_scores = torch.randn(batch_size, max_output_boxes)
        det_classes = torch.randint(0, num_classes, (batch_size, max_output_boxes), dtype=torch.int32)
        return num_det, det_boxes, det_scores, det_classes

    @staticmethod
    def symbolic(g,
                 boxes,
                 scores,
                 background_class=-1,
                 box_coding=0,
                 iou_threshold=0.45,
                 max_output_boxes=100,
                 plugin_version="1",
                 score_activation=0,
                 score_threshold=0.25):
        out = g.op("TRT::EfficientNMS_TRT",
                   boxes,
                   scores,
                   background_class_i=background_class,
                   box_coding_i=box_coding,
                   iou_threshold_f=iou_threshold,
                   max_output_boxes_i=max_output_boxes,
                   plugin_version_s=plugin_version,
                   score_activation_i=score_activation,
                   score_threshold_f=score_threshold,
                   outputs=4)
        nums, boxes, scores, classes = out
        return nums, boxes, scores, classes

class ONNX_TRT(nn.Module):
    '''onnx module with TensorRT NMS operation.'''
    def __init__(self, max_obj=100, iou_thres=0.45, score_thres=0.25, max_wh=None ,device=None, n_classes=80):
        super().__init__()
        assert max_wh is None
        self.device = device if device else torch.device('cpu')
        self.background_class = -1,
        self.box_coding = 1,
        self.iou_threshold = iou_thres
        self.max_obj = max_obj
        self.plugin_version = '1'
        self.score_activation = 0
        self.score_threshold = score_thres
        self.n_classes=n_classes

    def forward(self, x):
        boxes, confscores = x
        scores, classes = torch.max(confscores, 2, keepdim=True)
        print("boxes.shape ", boxes.shape)
        print("confscores.shape ", confscores.shape)
        num_det, det_boxes, det_scores, det_classes = TRT_NMS.apply(boxes, scores, self.background_class, self.box_coding,
                                                                    self.iou_threshold, self.max_obj,
                                                                    self.plugin_version, self.score_activation,
                                                                    self.score_threshold)
        return num_det, det_boxes, det_scores, det_classes


model_path = "yolo_nas_s.onnx"
onnx_export_kwargs = {
    'input_names' : ['images'],
    'output_names' : ["num_dets", "det_boxes", "det_scores", "det_classes"]
}

# net = models.get(Models.YOLO_NAS_L, pretrained_weights="coco")
best_model.eval()
end2end = ONNX_TRT()
end2end.eval()

models.convert_to_onnx(model=best_model, input_shape=(3,640,640), post_process=end2end, out_path=model_path,
                       torch_onnx_export_kwargs=onnx_export_kwargs)

# models.convert_to_onnx(model=net, input_shape=(3,640,640), post_process=end2end, out_path="yolo_nassss_s.onnx")