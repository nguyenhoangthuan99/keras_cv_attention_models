from keras_cv_attention_models.resnest.resnest import ResNest, ResNest50, ResNest101, ResNest200, ResNest269, rsoftmax, split_attention_conv2d


__head_doc__ = """
Keras implementation of [ResNeSt](https://github.com/zhanghang1989/ResNeSt).
Paper [PDF 2004.08955 ResNeSt: Split-Attention Networks](https://arxiv.org/pdf/2004.08955.pdf).
"""

__tail_doc__ = """  groups: controls number of split groups in `split_attention_conv2d`.
  input_shape: it should have exactly 3 inputs channels, like `(224, 224, 3)`.
      Set `(None, None, 3)` for dynamic input resolution.
  num_classes: number of classes to classify images into. Set `0` to exclude top layers.
  activation: activation used in whole model, default `relu`.
  classifier_activation: A `str` or callable. The activation function to use on the "top" layer if `num_classes > 0`.
      Set `classifier_activation=None` to return the logits of the "top" layer.
      Default is `softmax`.
  pretrained: one of `None` (random initialization) or 'imagenet' (pre-training on ImageNet).
      Will try to download and load pre-trained model weights if not None.
  **kwargs: other parameters if available.

Returns:
    A `keras.Model` instance.
"""

ResNest.__doc__ = __head_doc__ + """
Args:
  num_blocks: number of blocks in each stack.
  stem_width: output dimension after stem.
  model_name: string, model name.
""" + __tail_doc__ + """
Model architectures:
  | Model          | params | Image  resolution | Top1 Acc |
  | -------------- | ------ | ----------------- | -------- |
  | resnest50      | 28M    | 224               | 81.03    |
  | resnest101     | 49M    | 256               | 82.83    |
  | resnest200     | 71M    | 320               | 83.84    |
  | resnest269     | 111M   | 416               | 84.54    |
"""

ResNest50.__doc__ = __head_doc__ + """
Args:
""" + __tail_doc__

ResNest101.__doc__ = ResNest50.__doc__
ResNest200.__doc__ = ResNest50.__doc__
ResNest269.__doc__ = ResNest50.__doc__

split_attention_conv2d.__doc__ = __head_doc__ + """
Split-Attention. Callable function, NOT defined as a layer.

Args:
  inputs: input tensor.
  filters: output dimension.
  kernel_size: kernel size for grouped Conv2D.
  strides: strides for grouped Conv2D.
  groups: number of splitted groups.
  activation: activation used after `BatchNormalization`.

Examples:

>>> from keras_cv_attention_models import attention_layers
>>> inputs = keras.layers.Input([28, 28, 192])
>>> nn = attention_layers.split_attention_conv2d(inputs, 384)
>>> dd = keras.models.Model(inputs, nn)
>>> dd.summary()
>>> dd.output_shape
(None, 28, 28, 384)

>>> {ii.name: ii.shape for ii in dd.weights}
{'1_g1_conv/kernel:0': TensorShape([3, 3, 96, 384]),
 '1_g2_conv/kernel:0': TensorShape([3, 3, 96, 384]),
 '1_bn/gamma:0': TensorShape([768]),
 '1_bn/beta:0': TensorShape([768]),
 '1_bn/moving_mean:0': TensorShape([768]),
 '1_bn/moving_variance:0': TensorShape([768]),
 '2_conv/kernel:0': TensorShape([1, 1, 384, 96]),
 '2_conv/bias:0': TensorShape([96]),
 '2_bn/gamma:0': TensorShape([96]),
 '2_bn/beta:0': TensorShape([96]),
 '2_bn/moving_mean:0': TensorShape([96]),
 '2_bn/moving_variance:0': TensorShape([96]),
 '3_conv/kernel:0': TensorShape([1, 1, 96, 768]),
 '3_conv/bias:0': TensorShape([768])}
"""