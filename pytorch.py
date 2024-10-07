import keras2onnx
import onnx
from tensorflow.keras.models import load_model
import onnx
from onnx2pytorch import ConvertModel

# Load your Keras .h5 model
keras_model = load_model('quake.h5')

# Convert Keras model to ONNX format
onnx_model = keras2onnx.convert_keras(keras_model, keras_model.name)

# Save the ONNX model
onnx.save_model(onnx_model, 'temp.onnx')


# Load the ONNX model
onnx_model = onnx.load('temp.onnx')

# Convert ONNX to PyTorch
pytorch_model = ConvertModel(onnx_model)

# Now the pytorch_model can be used for inference or further training
pytorch_model.save('temp.pt')
