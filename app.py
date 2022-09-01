from weather_app.classifier import Classifier
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

def main():
    c = Classifier(filename="dataset.csv", class_attr="Play")
    print("Enter the correct values shown in the option! *Case Sensitive")
    print("Enter 'x' or 'exit' to exit from the system")
    outlook = input("Whats the weather outside? (Sunny, Rainy, Overcast):")
    if outlook.lower() == 'x' or outlook.lower() == 'exit':
        exitSystem()
    temp = input("Whats the temperature today? (Hot, Mild, Cool):")
    if temp.lower() == 'x' or temp.lower()== 'exit':
        exitSystem()
    humidity = input("Whats the humidity? (High, Normal):")
    if humidity.lower() == 'x' or humidity.lower()== 'exit':
        exitSystem()
    windy = input("Is it windy tody? (Yes or No):")
    if windy.lower() == 'x' or windy.lower()== 'exit':
        exitSystem()

    c.hypothesis = {"Outlook":outlook, "Temp":temp, "Humidity":humidity , "Windy":windy}
    c.calculate_priori()
    c.calculate_conditional_probabilities(c.hypothesis)
    c.classify()

if __name__ == "__main__":
    app.run()