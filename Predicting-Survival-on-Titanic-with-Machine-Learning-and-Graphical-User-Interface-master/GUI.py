import tkinter as tk
from tkinter import *
import tkinter.messagebox
from PIL import Image, ImageTk
import dataPreprocessing
import machineLearningModels
import pandas as pd
import tkinter.font as fd

class root(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry("1200x600+0+0")
        self.title("Titanic Disaster Platform")
        container = tk.Frame(self)
        
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 3)
        container.grid_columnconfigure(0, weight = 3)
      
        self.frames = {}

        for F in (StartPage, Page1, Page2, Page3, Page4, Page5, Page6):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky = "snew")
        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        load1 = Image.open('MLModelPics/bg2.png')
        render1 = ImageTk.PhotoImage(load1)
        img1 = tk.Label(self, image = render1)
        img1.image = render1
        img1.place(x = 0, y = 0)
        
        load2 = Image.open('MLModelPics/img1.jpg')
        render2 = ImageTk.PhotoImage(load2)
        img2 = tk.Label(self, image = render2)
        img2.image = render2
        img2.place(x = 65, y = 25)

        labelA = tk.Label(self, text= "These three buttons will help you understand\nand visualize the type of people that were on the Titanic\n by showing graphs of some interesting correlations\n that occur with survival/death rates\nand other passenger attributes.",bg='black',fg='white')
        labelA.place(x = 50, y = 300)

        buttonA = tk.Button(self, text = "Train Distribution", command = lambda: machineLearningModels.trainclassDistr(machineLearningModels.train_df),bg='grey')
        buttonA.place(x = 150, y = 400)

        buttonC = tk.Button(self, text = "Class Survival", command = lambda: machineLearningModels.trainClassSurvival(machineLearningModels.train_df),bg='grey')
        buttonC.place(x = 150, y = 450)

        buttonB = tk.Button(self, text = "Mean Fare Survival", command = lambda: machineLearningModels.trainMeanFareSurvival(machineLearningModels.train_df),bg='grey')
        buttonB.place(x = 150, y = 500)

        label = tk.Label(self , text= "Titanic Machine Learning from Disaster!",bg='black',fg='white',font=('Arial',25))
        label.place(x = 500, y = 150)
       
        button = tk.Button(self, text = "Log Regression", command = lambda: controller.show_frame(Page1),bg='#d3d3d3',height=2,width=18, font=('Arial',10,'bold'))
        button.place(x = 500, y = 300)
        
        button3 = tk.Button(self, text = "K Nearest Neighbor", command = lambda: controller.show_frame(Page2),bg='white',height=2,width=18, font=('Arial',10,'bold'))
        button3.place(x = 900, y = 300)
        
        button4 = tk.Button(self, text = "Random Forest", command = lambda: controller.show_frame(Page3),bg='white',height=2,width=18, font=('Arial',10,'bold'))
        button4.place(x = 500, y = 400)

        button5 = tk.Button(self, text = "Decision Tree", command = lambda: controller.show_frame(Page4),bg='white',height=2,width=18, font=('Arial',10,'bold'))
        button5.place(x = 900, y = 400)

        button7 = tk.Button(self, text = "Support Vector\nMachine", command = lambda: controller.show_frame(Page5),bg='white',height=2,width=18, font=('Arial',10,'bold'))
        button7.place(x = 500, y = 500)

        button8 = tk.Button(self, text = "Gaussian Naive\nBayes", command = lambda: controller.show_frame(Page6),bg='white',height=2,width=18, font=('Arial',10,'bold'))
        button8.place(x = 900, y = 500)

class Page1(tk.Frame):        
        def __init__(self, parent, controller):
                tk.Frame.__init__(self, parent)
                
                load1 = Image.open('MLModelPics/bg2.png')
                render1 = ImageTk.PhotoImage(load1)
                img1 = tk.Label(self, image = render1)
                img1.image = render1
                img1.place(x = 0, y = 0)

                load2 = Image.open('MLModelPics/LogRegression.jpg')
                load2 = load2.resize((499,307))
                render2 = ImageTk.PhotoImage(load2)
                img2 = tk.Label(self, image = render2)
                img2.image = render2
                img2.place(x = 600, y = 75)

                labelSum = tk.Label(self, text = "Logistic regression ",bg='black',fg='white',font=('Arial',40))
                labelSum.place(x =20, y= 20)

                textArea = tk.Text(self, height = 20, width = 15, wrap = tk.WORD)
                textArea.insert(tk.END, machineLearningModels.logRegression(machineLearningModels.train1, machineLearningModels.train2, machineLearningModels.test))
                textArea.configure(font=("Arial",12))

                scroller = tk.Scrollbar(self, orient= tk.VERTICAL,bg='Black')
                scroller.config(command = textArea.yview)
                textArea.configure(yscrollcommand= scroller.set)
                scroller.pack(side = tk.RIGHT, fill = tk.Y)
                textArea.place(x = 120, y = 100)

                labelScroll = tk.Label(self, text = "Hover over the predicition box and scroll\n down to see the model accuracy",bg='black',fg='white')
                labelScroll.place(x = 80, y= 480)

                button1 = tk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage),bg='grey')
                button1.place(x = 10, y = 550)

                buttonZ = tk.Button(self, text="Prediction Graph", command=lambda: machineLearningModels.groupPlot(machineLearningModels.predLog),bg='grey',height=5,width=15)
                buttonZ.place(x = 700, y = 500)


class Page2(tk.Frame):
        def __init__(self, parent, controller):
                tk.Frame.__init__(self, parent)
                
                load1 = Image.open('MLModelPics/bg2.png')
                render1 = ImageTk.PhotoImage(load1)
                img1 = tk.Label(self, image = render1)
                img1.image = render1
                img1.place(x = 0, y = 0)

                load2 = Image.open('MLModelPics/kNearestNeighbor.png')
                load2 = load2.resize((550,357))
                render2 = ImageTk.PhotoImage(load2)
                img2 = tk.Label(self, image = render2)
                img2.image = render2

                labelSum = tk.Label(self, text = "K-Nearest Neighbors",bg='black',fg='white',font=('Arial',40))
                labelSum.place(x =20, y= 20)

                img2.place(x = 600, y = 75)

                textArea = tk.Text(self, height = 20, width = 15, wrap = tk.WORD)
                textArea.insert(tk.END, machineLearningModels.KNN(machineLearningModels.train1, machineLearningModels.train2, machineLearningModels.test))
                textArea.configure(font=("Arial",12))

                scroller = tk.Scrollbar(self, orient= tk.VERTICAL)
                scroller.config(command = textArea.yview)
                textArea.configure(yscrollcommand= scroller.set)
                scroller.pack(side = tk.RIGHT, fill = tk.Y)
                textArea.place(x = 120, y = 100)

                labelScroll = tk.Label(self, text = "Hover over the predicition box and scroll\n down to see the model accuracy",bg='black',fg='white')
                labelScroll.place(x = 80, y= 480)

                button1 = tk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage),bg='grey')
                button1.place(x = 10, y = 550)

                buttonZ = tk.Button(self, text="Prediction Graph", command=lambda: machineLearningModels.groupPlot(machineLearningModels.predK),bg='grey',height=5,width=15)
                buttonZ.place(x = 700, y = 500)


class Page3(tk.Frame):
        def __init__(self, parent, controller):
                tk.Frame.__init__(self, parent)
                
                load1 = Image.open('MLModelPics/bg2.png')
                render1 = ImageTk.PhotoImage(load1)
                img1 = tk.Label(self, image = render1)
                img1.image = render1
                img1.place(x = 0, y = 0)

                load2 = Image.open('MLModelPics/rForest.png')
                load2 = load2.resize((499,340))
                render2 = ImageTk.PhotoImage(load2)
                img2 = tk.Label(self, image = render2)
                img2.image = render2
                img2.place(x = 600, y = 75)

                labelSum = tk.Label(self, text = "Random Forest",bg='black',fg='white',font=('Arial',40))
                labelSum.place(x =20, y= 20)

                textArea = tk.Text(self, height = 20, width = 15, wrap = tk.WORD)
                textArea.insert(tk.END, machineLearningModels.rForest(machineLearningModels.train1, machineLearningModels.train2, machineLearningModels.test))
                textArea.configure(font=("Arial",12))

                scroller = tk.Scrollbar(self, orient= tk.VERTICAL)
                scroller.config(command = textArea.yview)
                textArea.configure(yscrollcommand= scroller.set)
                scroller.pack(side = tk.RIGHT, fill = tk.Y)
                textArea.place(x = 120, y = 100)

                labelScroll = tk.Label(self, text = "Hover over the predicition box and scroll\n down to see the model accuracy",bg='black',fg='white')
                labelScroll.place(x = 80, y= 480)

                button1 = tk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage),bg='grey')
                button1.place(x = 10, y = 550)

                buttonZ = tk.Button(self, text="Prediction Graph", command=lambda: machineLearningModels.groupPlot(machineLearningModels.predForest),bg='grey',height=5,width=15)
                buttonZ.place(x = 700, y = 500)

class Page4(tk.Frame):
        def __init__(self, parent, controller):
                tk.Frame.__init__(self, parent)
                
                load1 = Image.open('MLModelPics/bg2.png')
                render1 = ImageTk.PhotoImage(load1)
                img1 = tk.Label(self, image = render1)
                img1.image = render1
                img1.place(x = 0, y = 0)

                load2 = Image.open('MLModelPics/DecisionTree.jpg')
                load2 = load2.resize((350, 350))
                render2 = ImageTk.PhotoImage(load2)
                img2 = tk.Label(self, image = render2)
                img2.image = render2
                img2.place(x = 600, y = 75)

                labelSum = tk.Label(self, text = "Decision tree",bg='black',fg='white',font=('Arial',40))
                labelSum.place(x =20, y= 20)


                textArea = tk.Text(self, height = 20, width = 15, wrap = tk.WORD)
                textArea.insert(tk.END, machineLearningModels.dTree(machineLearningModels.train1, machineLearningModels.train2, machineLearningModels.test))
                textArea.configure(font=("Arial",12))

                scroller = tk.Scrollbar(self, orient= tk.VERTICAL)
                scroller.config(command = textArea.yview)
                textArea.configure(yscrollcommand= scroller.set)
                scroller.pack(side = tk.RIGHT, fill = tk.Y)
                textArea.place(x = 120, y = 100)

                labelScroll = tk.Label(self, text = "Hover over the predicition box and scroll\n down to see the model accuracy",bg='black',fg='white')
                labelScroll.place(x = 80, y= 480)

                button1 = tk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage),bg='grey')
                button1.place(x = 10, y = 550)

                buttonZ = tk.Button(self, text="Prediction Graph", command=lambda: machineLearningModels.groupPlot(machineLearningModels.predTree),bg='grey',height=5,width=15)
                buttonZ.place(x = 700, y = 500)

class Page5(tk.Frame):
        def __init__(self, parent, controller):
                tk.Frame.__init__(self, parent)

                load1 = Image.open('MLModelPics/bg2.png')
                render1 = ImageTk.PhotoImage(load1)
                img1 = tk.Label(self, image = render1)
                img1.image = render1
                img1.place(x = 0, y = 0)

                load2 = Image.open('MLModelPics/LinearSUPPORTvector.png')
                load2 = load2.resize((500, 400))
                render2 = ImageTk.PhotoImage(load2)
                img2 = tk.Label(self, image = render2)
                img2.image = render2
                img2.place(x = 600, y = 75)


                labelSum = tk.Label(self, text = "Support Vector Machine",bg='black',fg='white',font=('Arial',40))
                labelSum.place(x =20, y= 20)

                textArea = tk.Text(self, height = 20, width = 15, wrap = tk.WORD)
                textArea.insert(tk.END, machineLearningModels.lSVM(machineLearningModels.train1, machineLearningModels.train2, machineLearningModels.test))
                textArea.configure(font=("Arial",12))

                scroller = tk.Scrollbar(self, orient= tk.VERTICAL)
                scroller.config(command = textArea.yview)
                textArea.configure(yscrollcommand= scroller.set)
                scroller.pack(side = tk.RIGHT, fill = tk.Y)
                textArea.place(x = 120, y = 100)

                labelScroll = tk.Label(self, text = "Hover over the predicition box and scroll\n down to see the model accuracy",bg='black',fg='white')
                labelScroll.place(x = 80, y= 480)

                button1 = tk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage),bg='grey')
                button1.place(x = 10, y = 550)

                buttonZ = tk.Button(self, text="Prediction Graph", command=lambda: machineLearningModels.groupPlot(machineLearningModels.predLSVM),bg='grey',height=5,width=15)
                buttonZ.place(x = 700, y = 500)

class Page6(tk.Frame):
        def __init__(self, parent, controller):
                tk.Frame.__init__(self, parent)

                load1 = Image.open('MLModelPics/bg2.png')
                render1 = ImageTk.PhotoImage(load1)
                img1 = tk.Label(self, image = render1)
                img1.image = render1
                img1.place(x = 0, y = 0)

                load2 = Image.open('MLModelPics/gNaiveBayes.png')
                load2 = load2.resize((550, 400))
                render2 = ImageTk.PhotoImage(load2)
                img2 = tk.Label(self, image = render2)
                img2.image = render2
                img2.place(x = 600, y = 75)

                labelSum = tk.Label(self, text = "Naive Bayes",bg='black',fg='white',font=('Arial',40))
                labelSum.place(x =20, y= 20)

                textArea = tk.Text(self, height = 20, width = 15, wrap = tk.WORD)
                textArea.insert(tk.END, machineLearningModels.gNaiveBayes(machineLearningModels.train1, machineLearningModels.train2, machineLearningModels.test))
                textArea.configure(font=("Arial",12))

                scroller = tk.Scrollbar(self, orient= tk.VERTICAL)
                scroller.config(command = textArea.yview)
                textArea.configure(yscrollcommand= scroller.set)
                scroller.pack(side = tk.RIGHT, fill = tk.Y)
                textArea.place(x = 120, y = 100)

                labelScroll = tk.Label(self, text = "Hover over the predicition box and scroll\n down to see the model accuracy",bg='black',fg='white')
                labelScroll.place(x = 80, y= 480)

                button1 = tk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage),bg='grey')
                button1.place(x = 10, y = 550)

                buttonZ = tk.Button(self, text="Prediction Graph", command=lambda: machineLearningModels.groupPlot(machineLearningModels.predBayes),bg='grey',height=5,width=15)
                buttonZ.place(x = 700, y = 500)

                
display = root()
display.mainloop()
