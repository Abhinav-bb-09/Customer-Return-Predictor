{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "3a247f5c-4323-4159-b00f-7a4a1d1f8d06",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "* Running on local URL:  http://127.0.0.1:7860\n",
      "* To create a public link, set `share=True` in `launch()`.\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div><iframe src=\"http://127.0.0.1:7860/\" width=\"100%\" height=\"500\" allow=\"autoplay; camera; microphone; clipboard-read; clipboard-write;\" frameborder=\"0\" allowfullscreen></iframe></div>"
      ],
      "text/plain": [
       "<IPython.core.display.HTML object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": []
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import gradio as gr\n",
    "import joblib\n",
    "import numpy as np\n",
    "\n",
    "# Load the model\n",
    "model = joblib.load(\"rfm_predictor.pkl\")\n",
    "\n",
    "# Define prediction function\n",
    "def predict_return(recency, frequency, monetary):\n",
    "    data = np.array([[recency, frequency, monetary]])\n",
    "    prediction = model.predict(data)[0]\n",
    "    return \"🟢 Likely to Return\" if prediction == 1 else \"🔴 May Not Return\"\n",
    "\n",
    "# Define Gradio Interface\n",
    "iface = gr.Interface(\n",
    "    fn=predict_return,\n",
    "    inputs=[\n",
    "        gr.Number(label=\"Recency (days)\"),\n",
    "        gr.Number(label=\"Frequency (total purchases)\"),\n",
    "        gr.Number(label=\"Monetary Value (total spent)\"),\n",
    "    ],\n",
    "    outputs=\"text\",\n",
    "    title=\"Customer Return Predictor\",\n",
    "    description=\"Enter RFM values to predict if a customer will likely return.\"\n",
    ")\n",
    "\n",
    "# Run locally or on HF\n",
    "iface.launch()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
