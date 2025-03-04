import os
from models.codeToPseudo.model_inference import *
from models.pseudoToCode.model_inference import *
from models.pseudoToCode.model_architecture import Transformer
import tensorflow_datasets as tfds

class PseudoToCode:
    def __init__(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))

        self.model_weights_path = os.path.join(current_dir, 'pseudoToCode', 'pseudoToCode.weights.h5')
        self.tokenizer_inputs_path = os.path.join(current_dir, 'pseudoToCode', 'tokenizer_inputs.pkl')
        self.tokenizer_outputs_path = os.path.join(current_dir, 'pseudoToCode', 'tokenizer_outputs.pkl')
        
        self.input_tokenizer, self.output_tokenizer = self.load_tokenizer()
        self.model = self.load_model()

        self.D_MODEL = 512 # 512
        self.N_LAYERS = 4 # 6
        self.FFN_UNITS = 512 # 2048
        self.N_HEADS = 8 # 8
        self.DROPOUT_RATE = 0.1 # 0.1
        self.MAX_LENGTH = 15  # Adding max length for sequences

    def load_model(self):
        try:
            # Recalculate tokens
            num_words_inputs = self.input_tokenizer.vocab_size + 2
            num_words_output = self.output_tokenizer.vocab_size + 2

            transformer = Transformer(
                vocab_size_enc=num_words_inputs,
                vocab_size_dec=num_words_output,
                d_model=self.D_MODEL,
                n_layers=self.N_LAYERS,
                FFN_units=self.FFN_UNITS,
                n_heads=self.N_HEADS,
                dropout_rate=self.DROPOUT_RATE
            )

            return transformer
        except Exception as e:
            print(f"Error loading model: {e}")
            return None

    def load_tokenizer(self):
        try:
            # Load tokenizers
            tokenizer_inputs = tfds.deprecated.text.SubwordTextEncoder.load_from_file(
                self.tokenizer_inputs_path
            )
            tokenizer_outputs = tfds.deprecated.text.SubwordTextEncoder.load_from_file(
                self.tokenizer_outputs_path
            )
            return tokenizer_inputs, tokenizer_outputs
        except Exception as e:
            print(f"Error loading tokenizers: {e}")
            return None, None

    def generate_code(self, pseudocode):
        try:
            # Generate the C++ code
            predictions = translate(self.model, pseudocode, self.input_tokenizer, self.output_tokenizer)
            return predictions
        except Exception as e:
            print(f"Error generating code: {e}")
            return f"Error generating code: {e}"