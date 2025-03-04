import os
from models.codeToPseudo.model_inference import *
import tensorflow_datasets as tfds
from models.codeToPseudo.model_architecture import Transformer

class CodeToPseudo:
    def __init__(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))

        self.model_weights_path = os.path.join(current_dir, 'codeToPseudo', 'codeToPseudo.weights.h5')
        self.tokenizer_inputs_path = os.path.join(current_dir, 'codeToPseudo', 'tokenizer_inputs.pkl')
        self.tokenizer_outputs_path = os.path.join(current_dir, 'codeToPseudo', 'tokenizer_outputs.pkl')
        
        self.model = self.load_model()
        self.input_tokenizer, self.output_tokenizer = self.load_tokenizer()

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
    
    def generate_pseudocode(self, cpp_code):
        try:
            # Generate the C++ code
            predictions = translate(self.model, cpp_code, self.input_tokenizer, self.output_tokenizer)
            return predictions
        except Exception as e:
            print(f"Error generating pseudocode: {e}")
            return f"Error generating pseudocode: {e}"