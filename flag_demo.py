import gradio as gr

def calculator(num1, operation, num2):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        return num1 / num2


iface = gr.Interface(
    fn=calculator,
    inputs=["number", gr.Radio(["add", "subtract", "multiply", "divide"]), "number"],
    outputs="number",
    allow_flagging="manual",
    title="Toy Calculator",
    description="Here's a sample toy calculator. Enjoy!",
    article="code can be found at https://github.com/aiplaybookin/gradio-demo"
)

iface.launch(share=True)