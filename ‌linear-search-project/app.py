import gradio as gr


def is_int(text):
    
    if text.startswith("-"):
        return text[1:].isdigit()
    return text.isdigit()



def linear_search(list_text, target_text):

    
    if not is_int(target_text):
        return "error: target must be an integer", ""

    target = int(target_text)

    
    parts = list_text.split(",")
    numbers = []

    
    index = 0
    while index < len(parts):
        item = parts[index].strip()

        
        if not is_int(item):
            return "error: list must contain only integers separated by commas", ""
        
        numbers.append(int(item))
        index += 1

    steps = []
    i = 0

    
    while i < len(numbers):
        steps.append(f"checking index {i}: value {numbers[i]}")
        
        if numbers[i] == target:
            steps.append(f"found {target} at index {i}")
            return "\n".join(steps), "done"
        
        i += 1

    steps.append(f"{target} not found")
    return "\n".join(steps), "done"



with gr.Blocks(title="linear search") as demo:
    gr.Markdown("# linear search")

    list_box = gr.Textbox(label="enter list", placeholder="example: 3, 8, 1, 7")
    target_box = gr.Textbox(label="enter target", placeholder="example: 7")

    run_button = gr.Button("run")

    step_box = gr.Textbox(label="steps", lines=12)
    result_box = gr.Textbox(label="result")

    run_button.click(
        linear_search,
        inputs=[list_box, target_box],
        outputs=[step_box, result_box]
    )

if __name__ == "__main__":
    demo.launch()
