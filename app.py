import gradio as gr
import os
import sys
import random 


def predict_toxicity(input_text):
    if not input_text:
        return {"status": "Please enter some text."}

    print(f"INFO: Running placeholder prediction for: '{input_text}'")
    
    try:
        
        result_dict = {
            "identity_hate": random.choice([True, False]),
            "insult": random.choice([True, False]),
            "obscene": random.choice([True, False]),
            "severe_toxic": random.choice([True, False]),
            "threat": random.choice([True, False]) if "bomb" not in input_text.lower() else True,
            "toxic": random.choice([True, False]) or ("threat" in result_dict and result_dict["threat"])
        }
        required_keys = {"identity_hate", "insult", "obscene", "severe_toxic", "threat", "toxic"}
        if not isinstance(result_dict, dict) or not required_keys.issubset(result_dict.keys()):
             print(f"ERROR: Model function returned unexpected format: {result_dict}")
             return {"error": "Model returned data in an unexpected format."}

        return result_dict 

    except Exception as e:
        print(f"Error during placeholder prediction: {e}")
        return {"error": f"An error occurred during analysis: {e}"}


# --- Gradio Interface ---
iface = gr.Interface(
    fn=predict_toxicity,             
    inputs=gr.Textbox(lines=5, placeholder="Enter text to check..."), 
    outputs=gr.JSON(),              
    title="YouTube Comment Toxicity Checker",
    description="Enter text to analyze its potential toxicity. Output shows classifications.",
    examples=[ 
        ["you are amazing and talented!"],
        ["i will plant a bomb in your house"]
    ],
    allow_flagging="never"
)

# --- Launching the Gradio App ---
if _name_ == "_main_":
    iface.launch(share=True)