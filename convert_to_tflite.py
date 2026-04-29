"""
Convert TensorFlow/Keras models to TensorFlow Lite format
Run this script locally to convert your existing models
"""

import os
import tensorflow as tf
from pathlib import Path

# Check if conversion is needed
model_dir = "models"  # Adjust if your models are in a different directory

if not os.path.exists(model_dir):
    print(f"Models directory '{model_dir}' not found!")
    exit(1)

# Convert .h5 or SavedModel to .tflite
for model_file in Path(model_dir).glob("**/*"):
    if model_file.suffix in ['.h5', '.keras']:
        print(f"Converting {model_file}...")
        try:
            # Load the model
            model = tf.keras.models.load_model(str(model_file))
            
            # Convert to TFLite
            converter = tf.lite.TFLiteConverter.from_keras_model(model)
            converter.optimizations = [tf.lite.Optimize.DEFAULT]
            tflite_model = converter.convert()
            
            # Save as .tflite
            output_file = model_file.with_suffix('.tflite')
            with open(output_file, 'wb') as f:
                f.write(tflite_model)
            
            print(f"✓ Converted to {output_file}")
        except Exception as e:
            print(f"✗ Error converting {model_file}: {e}")
    
    elif str(model_file).endswith('saved_model.pb'):
        print(f"Converting SavedModel from {model_file.parent}...")
        try:
            converter = tf.lite.TFLiteConverter.from_saved_model(str(model_file.parent))
            converter.optimizations = [tf.lite.Optimize.DEFAULT]
            tflite_model = converter.convert()
            
            output_file = model_file.parent / "model.tflite"
            with open(output_file, 'wb') as f:
                f.write(tflite_model)
            
            print(f"✓ Converted to {output_file}")
        except Exception as e:
            print(f"✗ Error converting SavedModel: {e}")

print("\nConversion complete! Upload .tflite files to your deployment.")
