from tkinter import*
import math,random,os
from tkinter import messagebox
from datetime import datetime
import os, sys
import re
import tkinter as tk
from tkinter import ttk
import pymysql
from PIL import ImageTk
from PIL import Image 
from tkinter import  filedialog

##############################################
import sys; sys.path
import pandas as pd
from collections import defaultdict
############################################## 
import xlsxwriter
import csv
from openpyxl import Workbook

#Webcam related
import cv2

import PyQt5.QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QImage, QPixmap, QIcon

#######################LATEST for text and image to PDF
#Convert text file to pdf file
from fpdf import FPDF
#for image
import fitz 


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Newly added
#This function will happen once there is a quit!
def login_quit():
	ask=messagebox.askyesno("Quitting Application","Are you sure to proceed with Quitting! \nGoodbye!")
	if ask==True:
		master.destroy()

#This function will happen once the login is valid
def user_valid():
	global v, n
	v=ery2.get()
	n=ery3.get()
	global root
	try:
		if v.lower()=="admin" and n=="P@55#0rd" or v.lower()=="user" and n=="lgaverify" :      
			#Exit the login dialog
			master.destroy()

			category = {"BORNO": ['ABADAM','ASKIRA/UBA','BAMA','BAYO','BIU','CHIBOK','DAMBOA','DIKWA','GUBIO',
									'GUZAMALA','GWOZA','HAWUL','JERE','KAGA','KALA/BALGE','KONDUGA','KUKAWA',
									'KWAYA KUSAR','MAFA','MAGUMERI','MAIDUGURI','MARTE','MOBBAR','MONGUNO','NGALA','NGANZAI','SHANI'],
						"": ['']			
									}
									
			class BORNO_App:
				
				def __init__(self,root):
					self.root=root
					mydata=[]
					#Title of the Application
					self.root.title("Verification & Payment of Gratuity Application @2020")
					self.root.wm_iconbitmap('icon.ico')
					
					#This code enables the app to open in a maximized state
					root.state('zoomed')
					
					#I used the code below to ensure the app zooms to any system in use resolution
					width, height = root.winfo_screenwidth(), root.winfo_screenheight()
					root.geometry('%dx%d+0+0' % (width,height))
					
					#Assigning a Background Color to a Variable bg_color
					#bg_color="#074463"
					global bg_color
					bg_color="DarkGray"
					#The heading of the application
					#Text, Border, Style, Font Type, Size, Style, Background and Foreground Colors
					title=Label(self.root,text="COMMITTEE ON VERIFICATION OF LOCAL GOVT. PENSIONERS & PAYMENT OF GRATUITY",bd=8,relief=GROOVE,font=("arial black",20,"bold"),bg="DarkGray",fg="DarkGreen")
					title.pack(side=TOP,fill=X)
					
					#=======================All Variables
					self.FormNo=StringVar()
					self.LGAofRetire=StringVar()
					self.Identity=StringVar()
					self.FirstName=StringVar()
					self.MiddleName=StringVar()
					self.Surname=StringVar()
					self.Gender=StringVar()
					self.DOB=StringVar()
					self.DOofFAP=StringVar()
					self.Rank=StringVar()
					self.Grade=StringVar()
					self.Step=StringVar()
					self.DOR=StringVar()
					self.CurrentStatus=StringVar()
					self.DOD=StringVar()		
					self.State=StringVar()
					self.LGA=StringVar()
					self.Qualification=StringVar()
					self.DOQ=StringVar()
					self.SalaryPenMonth=StringVar()
					self.GratuityBalance=StringVar()
					self.PensionArrest=StringVar()
					self.FileNoLASGLG=StringVar()
					self.Bank=StringVar()
					self.Account=StringVar()
					self.BVN=StringVar()
					self.Address=StringVar()
					self.Phone=StringVar()
					self.IdentifiedName=StringVar()
					self.PayStatus=StringVar()
					self.PayDate=StringVar()
					self.search_by=StringVar()
					self.search_txt=StringVar()		
					self.photo_txt=StringVar()
					self.SecureCode=StringVar()
					
					#From To
					self.ToYear=StringVar()
					self.FromYear=StringVar()
					
					#Camera Image
					self.logic=0
					#self.value=1
					#self.TEXT.setText('Kindly Press "Show" to connect with webcam.')
					
					#=======================Staff detail frame
					F1=LabelFrame(self.root,bd=8,relief=GROOVE,text="LGA Retiree Details",font=("Arial",15,"bold"),fg="DarkRed",bg=bg_color)
					#F1.place(x=0,y=55,width=700,height=740)
					F1.place(x=0,y=55,relwidth=1,height=385)
					
					global FormNo_txt
					#FormNo Number 
					FormNo_lbl=Label(F1,text="Form No:.",bg=bg_color,fg="blue",font=("times new roman",15,"bold")).grid(row=0,column=0,padx=18,pady=1,sticky="w")	
					FormNo_txt=Entry(F1,width=18,textvariable=self.FormNo,font="arial 10 bold",bd=3,relief=SUNKEN)
					FormNo_txt.grid(row=0,column=1,padx=5,pady=1)
					FormNo_txt.focus()
					
					#LGA of Retire 
					LGAofRetire_lbl=Label(F1,text="LGA of Retire",bg=bg_color,fg="black",font=("times new roman",15,"bold")).grid(row=0,column=2,padx=18,pady=1,sticky="w")	
					#t1_txt=Entry(F1,width=18,textvariable=self.LGAofRetire,font="arial 10 bold",bd=3,relief=SUNKEN).grid(row=2,column=1,padx=5,pady=1)
					combo_LGAofRetire=ttk.Combobox(F1,textvariable=self.LGAofRetire,width=16,font="arial 10 bold",state='readonly')
					combo_LGAofRetire['values']=('ABADAM','ASKIRA/UBA','BAMA','BAYO','BIU','CHIBOK','DAMBOA','DIKWA','GUBIO',
									'GUZAMALA','GWOZA','HAWUL','JERE','KAGA','KALA/BALGE','KONDUGA','KUKAWA',
									'KWAYA KUSAR','MAFA','MAGUMERI','MAIDUGURI','MARTE','MOBBAR','MONGUNO','NGALA','NGANZAI','SHANI')
					combo_LGAofRetire.grid(row=0,column=3,padx=5,pady=1,sticky="w")
					
					
					#Name 
					Name_lbl=Label(F1,text="FirstName",bg=bg_color,fg="black",font=("times new roman",15,"bold")).grid(row=1,column=0,padx=18,pady=1,sticky="w")	
					Name_txt=Entry(F1,width=18,textvariable=self.FirstName,font="arial 10 bold",bd=3,relief=SUNKEN).grid(row=1,column=1,padx=5,pady=1)

					#MiddleName 
					MiddleName_lbl=Label(F1,text="MiddleName",bg=bg_color,fg="black",font=("times new roman",15,"bold")).grid(row=1,column=2,padx=18,pady=1,sticky="w")	
					MiddleName_txt=Entry(F1,width=18,textvariable=self.MiddleName,font="arial 10 bold",bd=3,relief=SUNKEN).grid(row=1,column=3,padx=5,pady=1)
					
					#Surname 
					Surname_lbl=Label(F1,text="Surname",bg=bg_color,fg="black",font=("times new roman",15,"bold")).grid(row=1,column=4,padx=18,pady=1,sticky="w")	
					Surname_txt=Entry(F1,width=18,textvariable=self.Surname,font="arial 10 bold",bd=3,relief=SUNKEN).grid(row=1,column=5,padx=5,pady=1)
					
					#Gender 
					Gender_lbl=Label(F1,text="Gender",bg=bg_color,fg="black",font=("times new roman",15,"bold")).grid(row=2,column=0,padx=18,pady=1,sticky="w")	
					#t1_txt=Entry(F1,width=18,textvariable=self.Gender,font="arial 10 bold",bd=3,relief=SUNKEN).grid(row=2,column=1,padx=18,pady=1)
					combo_Gender=ttk.Combobox(F1,textvariable=self.Gender,width=16,font="arial 10 bold",state='readonly')
					combo_Gender['values']=("MALE","FEMALE")
					combo_Gender.grid(row=2,column=1,padx=5,pady=1,sticky="w")
					
					global DOB_txt
					#DOB
					DOB_lbl=Label(F1,text="DateBirth",bg=bg_color,fg="black",font=("times new roman",15,"bold")).grid(row=2,column=2,padx=18,pady=1,sticky="w")	
					DOB_txt=Entry(F1,width=18,textvariable=self.DOB,font="arial 10 bold",bd=3,relief=SUNKEN)
					DOB_txt.grid(row=2,column=3,padx=5,pady=1)
					DOB_txt.focus()

					global DOofFAP_txt
					#DOofFAP
					DOofFAP_lbl=Label(F1,text="Date1stApp",bg=bg_color,fg="black",font=("times new roman",15,"bold")).grid(row=2,column=4,padx=18,pady=1,sticky="w")	
					DOofFAP_txt=Entry(F1,width=18,textvariable=self.DOofFAP,font="arial 10 bold",bd=3,relief=SUNKEN)
					DOofFAP_txt.grid(row=2,column=5,padx=5,pady=1)
					DOofFAP_txt.focus()
					
					#Rank
					Rank_lbl=Label(F1,text="Rank",bg=bg_color,fg="black",font=("times new roman",15,"bold")).grid(row=3,column=0,padx=18,pady=1,sticky="w")	
					Rank_txt=Entry(F1,width=18,textvariable=self.Rank,font="arial 10 bold",bd=3,relief=SUNKEN).grid(row=3,column=1,padx=5,pady=1)
					
					#GradeLevel 
					GradeLevel_lbl=Label(F1,text="Grade",bg=bg_color,fg="black",font=("times new roman",15,"bold")).grid(row=3,column=2,padx=18,pady=1,sticky="w")	
					GradeLevel_txt=Entry(F1,width=18,textvariable=self.Grade,font="arial 10 bold",bd=3,relief=SUNKEN).grid(row=3,column=3,padx=5,pady=1)

					#StepLevel 
					StepLevel_lbl=Label(F1,text="Step",bg=bg_color,fg="black",font=("times new roman",15,"bold")).grid(row=3,column=4,padx=18,pady=1,sticky="w")	
					StepLevel_txt=Entry(F1,width=18,textvariable=self.Step,font="arial 10 bold",bd=3,relief=SUNKEN).grid(row=3,column=5,padx=5,pady=1)
				
					global DOR_txt
					#DOR 
					DOR_lbl=Label(F1,text="DateRetire",bg=bg_color,fg="black",font=("times new roman",15,"bold")).grid(row=4,column=0,padx=18,pady=1,sticky="w")	
					DOR_txt=Entry(F1,width=18,textvariable=self.DOR,font="arial 10 bold",bd=3,relief=SUNKEN)
					DOR_txt.grid(row=4,column=1,padx=5,pady=1)
					DOR_txt.focus()
				
					#Status 
					CurrentStatus_lbl=Label(F1,text="Current Status",bg=bg_color,fg="black",font=("times new roman",15,"bold")).grid(row=4,column=2,padx=18,pady=1,sticky="w")	
					combo_CurrentStatus=ttk.Combobox(F1,textvariable=self.CurrentStatus,width=16,font="arial 10 bold",state='readonly')
					combo_CurrentStatus['values']=("ALIVE   ","DECEASED")
					combo_CurrentStatus.bind('<<ComboboxSelected>>', self.getUpdateStatus)
					combo_CurrentStatus.grid(row=4,column=3,padx=5,pady=1,sticky="w")

					global DOD_txt
					#DOD 
					DOD_lbl=Label(F1,text="D.Death",bg=bg_color,fg="black",font=("times new roman",15,"bold")).grid(row=4,column=4,padx=18,pady=1,sticky="w")	
					DOD_txt=Entry(F1,width=18,textvariable=self.DOD,font="arial 10 bold",bd=3,relief=SUNKEN,state='readonly')
					DOD_txt.grid(row=4,column=5,padx=5,pady=1)
					DOD_txt.focus()		

				
					#Globalize variables for State and LGA
					global combo_State, combo_LGA
					
					#State 
					State_lbl=Label(F1,text="State of Origin",bg=bg_color,fg="black",font=("times new roman",15,"bold")).grid(row=5,column=0,padx=18,pady=1,sticky="w")	
					#State_txt=Entry(F1,width=18,textvariable=self.State,font="arial 10 bold",bd=3,relief=SUNKEN).grid(row=2,column=3,padx=5,pady=1)
					combo_State=ttk.Combobox(F1,textvariable=self.State,width=16,font=("Arial",10,"bold"))
					combo_State['values'] = list(category.keys())
					combo_State.bind('<<ComboboxSelected>>', self.getUpdateData)
					combo_State.grid(row=5,column=1,pady=2,padx=5,sticky="w")
					
					#LGA 
					LGA_lbl=Label(F1,text="LGA",bg=bg_color,fg="black",font=("times new roman",15,"bold")).grid(row=5,column=2,padx=18,pady=1,sticky="w")	
					#LGA_txt=Entry(F1,width=18,textvariable=self.LGA,font="arial 10 bold",bd=3,relief=SUNKEN).grid(row=2,column=5,padx=5,pady=1)
					combo_LGA=ttk.Combobox(F1,textvariable=self.LGA,width=16,font=("Arial",10,"bold"))					
					combo_LGA.grid(row=5,column=3,pady=2,padx=5,sticky="w")

					
					#Qualification 
					Qualification_lbl=Label(F1,text="Qualification",bg=bg_color,fg="black",font=("times new roman",15,"bold")).grid(row=5,column=4,padx=18,pady=1,sticky="w")	
					combo_Qualification=ttk.Combobox(F1,textvariable=self.Qualification,width=16,font="arial 10 bold")
					combo_Qualification['values']=("MSc.","B.Sc.","HND","ND","NCE","SSCE")
					combo_Qualification.grid(row=5,column=5,padx=5,pady=1,sticky="w")

					global DOQ_txt
					#DOQ 
					DOQ_lbl=Label(F1,text="Date Qual.",bg=bg_color,fg="black",font=("times new roman",15,"bold")).grid(row=6,column=0,padx=18,pady=1,sticky="w")	
					DOQ_txt=Entry(F1,width=18,textvariable=self.DOQ,font="arial 10 bold",bd=3,relief=SUNKEN)
					DOQ_txt.grid(row=6,column=1,padx=5,pady=1)
					DOQ_txt.focus()

					#SalaryPenMonth 
					SalaryPenMonth_lbl=Label(F1,text="SalaryPenMonth",bg=bg_color,fg="black",font=("times new roman",15,"bold")).grid(row=6,column=2,padx=18,pady=1,sticky="w")	
					SalaryPenMonth_txt=Entry(F1,width=18,textvariable=self.SalaryPenMonth,font="arial 10 bold",bd=3,relief=SUNKEN).grid(row=6,column=3,padx=5,pady=1)

					#Gratuity 
					Gratuity_lbl=Label(F1,text="Bal.Gratuity",bg=bg_color,fg="black",font=("times new roman",15,"bold")).grid(row=6,column=4,padx=18,pady=1,sticky="w")	
					Gratuity_txt=Entry(F1,width=18,textvariable=self.GratuityBalance,font="arial 10 bold",bd=3,relief=SUNKEN).grid(row=6,column=5,padx=5,pady=1)
					
					#PensionArrest
					PensionArrest_lbl=Label(F1,text="Outs.Pension",bg=bg_color,fg="black",font=("times new roman",15,"bold")).grid(row=7,column=0,padx=18,pady=1,sticky="w")	
					PensionArrest_txt=Entry(F1,width=18,textvariable=self.PensionArrest,font="arial 10 bold",bd=3,relief=SUNKEN).grid(row=7,column=1,padx=5,pady=1)

					#FileNoLASGLG
					FileNoLASGLG_lbl=Label(F1,text="FileNo.LASGLG",bg=bg_color,fg="black",font=("times new roman",15,"bold")).grid(row=7,column=2,padx=18,pady=1,sticky="w")	
					#FileNoLASGLG_txt=Entry(F1,width=60,textvariable=self.FileNoLASGLG,font="arial 10 bold",bd=3,relief=SUNKEN).grid(row=7,column=3,columnspan=3,padx=5,pady=1)
					FileNoLASGLG_txt=Entry(F1,width=18,textvariable=self.FileNoLASGLG,font="arial 10 bold",bd=3,relief=SUNKEN).grid(row=7,column=3,padx=5,pady=1)

					
					#Bank 
					Bank_lbl=Label(F1,text="Bank",bg=bg_color,fg="black",font=("times new roman",15,"bold")).grid(row=7,column=4,padx=18,pady=1,sticky="w")	
					#Bank_txt=Entry(F1,width=25,textvariable=self.Bank,font="arial 10 bold",bd=3,relief=SUNKEN).grid(row=0,column=11,columnspan=2,padx=5,pady=1)
					combo_bank=ttk.Combobox(F1,textvariable=self.Bank,width=16,font="arial 10 bold",state='readonly')
					combo_bank['values']=("ACCESS","AGRIC BANK","DIAMOND","ECOBANK","FCMB","FIDELITY","FIRST",
											"GTBANK","HERITAGE","JAIZ","KEYSTONE","SKYE","POLARIS",
											"STANBIC","STERLING","UBA PLC","UNION","UNITY","ZENITH")
					combo_bank.grid(row=7,column=5,padx=5,pady=1,sticky="w")
					
					global Account_txt
					#Account 
					Account_lbl=Label(F1,text="Account",bg=bg_color,fg="black",font=("times new roman",15,"bold")).grid(row=8,column=0,padx=18,pady=1,sticky="w")	
					Account_txt=Entry(F1,width=18,textvariable=self.Account,font="arial 10 bold",bd=3,relief=SUNKEN)
					Account_txt.grid(row=8,column=1,padx=5,pady=1)
					Account_txt.focus()

					global BVN_txt
					#BVN 
					BVN_lbl=Label(F1,text="BVN",bg=bg_color,fg="black",font=("times new roman",15,"bold")).grid(row=8,column=2,padx=18,pady=1,sticky="w")	
					BVN_txt=Entry(F1,width=18,textvariable=self.BVN,font="arial 10 bold",bd=3,relief=SUNKEN)
					BVN_txt.grid(row=8,column=3,padx=5,pady=1)
					BVN_txt.focus()
					
					global combo_Identity
					#Identity 
					Identity_lbl=Label(F1,text="Identity/Kin",bg=bg_color,fg="black",font=("times new roman",15,"bold")).grid(row=8,column=4,padx=18,pady=1,sticky="w")	
					combo_Identity=ttk.Combobox(F1,textvariable=self.Identity,width=16,font="arial 10 bold",state='readonly')
					combo_Identity['values']=('SELF','WIFE','SON','DAUGHTER','OTHER')
					#A function will take an event when any of the above item is selected
					combo_Identity.bind('<<ComboboxSelected>>', self.getUpdateIdentity)
					combo_Identity.grid(row=8,column=5,padx=5,pady=1,sticky="w")
					combo_Identity.focus()
					
					global IdentityKinName_txt
					#Address 
					IdentityKinName_lbl=Label(F1,text="Identified Name",bg=bg_color,fg="black",font=("times new roman",15,"bold")).grid(row=9,column=0,padx=18,pady=1,sticky="w")	
					IdentityKinName_txt=Entry(F1,width=65,textvariable=self.IdentifiedName,font="arial 10 bold",bd=3,relief=SUNKEN,state='readonly')
					IdentityKinName_txt.grid(row=9,column=1,columnspan=3,padx=1,pady=1)

					#Phone 
					Phone1_lbl=Label(F1,text="Phone",bg=bg_color,fg="black",font=("times new roman",15,"bold")).grid(row=9,column=4,padx=18,pady=1,sticky="w")	
					Phone1_txt=Entry(F1,width=18,textvariable=self.Phone,font="arial 10 bold",bd=3,relief=SUNKEN).grid(row=9,column=5,padx=5,pady=1)

					#Address 
					Address_lbl=Label(F1,text="Address",bg=bg_color,fg="black",font=("times new roman",15,"bold")).grid(row=10,column=0,padx=18,pady=1,sticky="w")	
					Address_txt=Entry(F1,width=65,textvariable=self.Address,font="arial 10 bold",bd=3,relief=SUNKEN).grid(row=10,column=1,columnspan=3,padx=1,pady=1)
					
					##Phone2 
					##Phone2_lbl=Label(F1,text="Phone2",bg=bg_color,fg="black",font=("times new roman",15,"bold")).grid(row=10,column=2,padx=18,pady=1,sticky="w")	
					##Phone2_txt=Entry(F1,width=18,textvariable=self.Phone2,font="arial 10 bold",bd=3,relief=SUNKEN).grid(row=10,column=3,padx=5,pady=1)		

					#PayStatus 
					PayStatus_lbl=Label(F1,text="Pay Status",bg=bg_color,fg="black",font=("times new roman",15,"bold")).grid(row=10,column=4,padx=18,pady=1,sticky="w")	
					combo_PayStatus=ttk.Combobox(F1,textvariable=self.PayStatus,width=16,font="arial 10 bold",state='readonly')
					combo_PayStatus['values']=("PAID","UNPAID")
					combo_PayStatus.grid(row=10,column=5,padx=5,pady=1,sticky="w")
					
							
					#Net readonly mode
					#PayDate_lbl=Label(F1,text="Capture Date",bg=bg_color,fg="blue",font=("times new roman",15,"bold")).grid(row=9,column=6,padx=1,pady=1,sticky="w")	
					PayDate_txt=Entry(F1,width=30,textvariable=self.PayDate,fg="red",font="arial 10 bold",bd=5,relief=GROOVE,state='readonly')
					PayDate_txt.grid(row=10,column=7,pady=0,padx=5,sticky="w")
					
					global passport_Frame	
					#Passport Frame ****************************************
					#This frame is segmented area for Passport
					passport_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="Gray")
					passport_Frame.place(x=965,y=80,width=219,height=240)
					
					#Add Passport Frame ****************************************
					#This frame is segmented area for Add Passport
					addpassport_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="Gray")
					addpassport_Frame.place(x=965,y=320,width=220,height=40)
					
					#Add image from storage
					Addbtn=Button(addpassport_Frame,text="Add Pix",width=8,fg="Blue",font=("Arial",9,"bold"),command=self.OpenImage).grid(row=0,column=0,padx=4,pady=3)
					#Add image from webcam
					Cambtn=Button(addpassport_Frame,text="Cam Pix",width=7,fg="Blue",font=("Arial",9,"bold"),command=self.onClicked).grid(row=0,column=1,padx=4,pady=3)
					
					#CaptureCambtn=Button(addpassport_Frame,text="Capture",width=7,fg="Blue",font=("Arial",9,"bold"),command=self.CapturedClicked).grid(row=0,column=2,padx=4,pady=3)

					ClearCaptureCambtn=Button(addpassport_Frame,text="ClearPix",width=7,fg="Blue",font=("Arial",9,"bold"),command=self.ClearCapturedClicked).grid(row=0,column=2,padx=4,pady=3)
					
					##global camImage
					##camImage=Label(F1,width=20).grid(row=0,column=8,rowspan=2,padx=5,pady=5)
					
					
					
					#=======================Control frame
					btn_Frame=LabelFrame(self.root,bd=8,relief=RIDGE,bg=bg_color)
					btn_Frame.place(x=0,y=435,width=370,height=55)
					
					#Adding buttons to perform different actions
					#Different commands will be added to this buttons to perform actions upon click
					#The add_staff function will be added to Addbtn: command=self.add_staff (test it, confirm data in DB)
					Addbtn=Button(btn_Frame,text="Add",width=7,command=self.add_record,fg="Blue",font=("Arial",12,"bold")).grid(row=0,column=0,padx=4,pady=3)
					
					#The update function will be added here to Updatebtn: command=self.update_data
					Updatebtn=Button(btn_Frame,text="Update",width=7,command=self.UpdateDB_data,fg="Green",font=("Arial",12,"bold")).grid(row=0,column=1,padx=4,pady=3)
					
					#The delete function will be added here to Deletebtn: command=self.delete_data 
					Deletebtn=Button(btn_Frame,text="Delete",width=7,command=self.delete_data,fg="Red",font=("Arial",12,"bold")).grid(row=0,column=2,padx=4,pady=3)
					
					#The clear function will be added to Clearbtn: command=self.clear to enable clear the visible data
					Clearbtn=Button(btn_Frame,text="Clear",width=7,command=self.Clear_data,fg="Black",font=("Arial",12,"bold")).grid(row=0,column=3,padx=4,pady=3)
					
					Photo_url=Entry(F1,textvariable=self.photo_txt,fg="White",bg="White",width=30,font=("Arial",10,"bold"),bd=5,relief=GROOVE,state='readonly')
					Photo_url.grid(row=9,column=7,pady=0,padx=5,sticky="w")
					
					#=======================Seperator frame
					Seperator_Frame=LabelFrame(self.root,bd=8,relief=GROOVE,bg=bg_color)
					Seperator_Frame.place(x=375,y=435,width=75,height=55)		
					
					#=======================Search frame
					btn_Frame2=LabelFrame(self.root,bd=8,relief=RIDGE,bg=bg_color)
					btn_Frame2.place(x=450,y=435,relwidth=1,height=55)
					
					FetchAllDB_btn=Button(btn_Frame2,text="Show ALL",command=self.fetch_data,width=8,bd=3,bg=bg_color,fg="DarkRed",font="arial 12 bold").grid(row=0,column=0,padx=2,pady=2)
								
					#NEWLY to Search DB
					#ComboBox for Text area select kind of data to search
					combo_Search_By=ttk.Combobox(btn_Frame2,textvariable=self.search_by,width=11,font=("Arial",15,"normal"))
					#All variables for search
					combo_Search_By['values']=("FormNo","LGAofRetire","FirstName","MiddleName","Surname","Gender","DateBirth","DateFAP","Rank","Grade","Step","DateRetire","CurrentStatus","DateDeath","State","LGAOrigin","Qualification","DateQual","SalaryPenMonth","GratuityBalance","PensionArrest","FileNoLASGLG","Bank","Account","BVN","Identity","IdentifiedName","Phone","Address","PayStatus","PayDate","SecureCode")
							
					#Position of combo box
					combo_Search_By.grid(row=0,column=1,padx=2,pady=2)
					
					#Text Space to Type Data for Search
					#Addition of textvariable=self.search_txt
					txt_Search_Txt=Entry(btn_Frame2,textvariable=self.search_txt,width=21,bg="LightGray",fg="DarkBlue",font=("Arial",15,"normal"),bd=5,relief=GROOVE)
					txt_Search_Txt.grid(row=0,column=2,pady=2,padx=2,sticky="w")
					
					#Button to Search DB
					#This button works with the Combo Search and Search text above
					#They must comply
					Search_btn=Button(btn_Frame2,text="Search DB",command=self.search_data,width=9,bd=3,font="arial 12 bold").grid(row=0,column=4,padx=2,pady=2)
					
					################################################
					#Save to Excel
					global CurrentViewToExcel_btn                    
					CurrentViewToExcel_btn=Button(btn_Frame2,text="To Excel",command=self.SaveCurrentTableItem,width=9,bd=3,fg="Green",font="arial 12 bold")
					CurrentViewToExcel_btn.grid(row=0,column=5,padx=2,pady=2)
					##CurrentViewToExcel_btn['state']='disabled'		
					
					#Print File
					global Print_btn                    
					Print_btn=Button(btn_Frame2,text="Print Txt",command=self.print_bill,width=7,bd=3,fg="Red",font="arial 12 bold")
					Print_btn.grid(row=0,column=6,padx=2,pady=2)
					
					#Print PDF with Image File
					global PrintPDFandImage_btn                    
					PrintPDFandImage_btn=Button(btn_Frame2,text="Print PDF",command=self.print_pdfbill,width=8,bd=3,fg="Blue",font="arial 12 bold")
					PrintPDFandImage_btn.grid(row=0,column=7,padx=2,pady=2)
					
					
					#=======================Table Frame
					Table_Frame=LabelFrame(self.root,bd=8,relief=RIDGE,bg=bg_color)
					Table_Frame.place(x=0,y=490,width=940,height=175)
					
					#DISPLAY FOR ALL BILL ENTRY
					scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
					scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
					#Format for the required column headings that will be displayed
					self.Staff_table=ttk.Treeview(Table_Frame,columns=("FormNo","LGAofRetire","FirstName","MiddleName","Surname","Gender","DateBirth","DateFAP","Rank","Grade","Step","DateRetire","CurrentStatus","DateDeath","State","LGAOrigin","Qualification","DateQual","SalaryPenMonth","GratuityBalance","PensionArrest","FileNoLASGLG","Bank","Account","BVN","Identity","IdentifiedName","Phone","Address","PayStatus","PayDate","Photo","FromYear","ToYear","SecureCode"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
					
					#Scroll bar direction and configuration
					scroll_x.pack(side=BOTTOM,fill=X)
					scroll_y.pack(side=RIGHT,fill=Y)
					scroll_x.config(command=self.Staff_table.xview)
					scroll_y.config(command=self.Staff_table.yview)		
					
					#Connecting each heading to a column of the existing fields
					self.Staff_table.heading("FormNo",text="FormNo")
					self.Staff_table.heading("LGAofRetire",text="LGAofRetire")
					self.Staff_table.heading("FirstName",text="FirstName")
					self.Staff_table.heading("MiddleName",text="MiddleName")
					self.Staff_table.heading("Surname",text="Surname")
					self.Staff_table.heading("Gender",text="Gender")
					self.Staff_table.heading("DateBirth",text="DateBirth")
					self.Staff_table.heading("DateFAP",text="DateFAP")
					self.Staff_table.heading("Rank",text="Rank")
					self.Staff_table.heading("Grade",text="Grade")
					self.Staff_table.heading("Step",text="Step")
					self.Staff_table.heading("DateRetire",text="DateRetire")
					self.Staff_table.heading("CurrentStatus",text="CurrentStatus")
					self.Staff_table.heading("DateDeath",text="DateDeath")
					self.Staff_table.heading("State",text="State")
					self.Staff_table.heading("LGAOrigin",text="LGAOrigin")
					self.Staff_table.heading("Qualification",text="Qualification")
					self.Staff_table.heading("DateQual",text="DateQual")
					self.Staff_table.heading("SalaryPenMonth",text="SalaryPenMonth")
					self.Staff_table.heading("GratuityBalance",text="GratuityBalance")
					self.Staff_table.heading("PensionArrest",text="PensionArrest")
					self.Staff_table.heading("FileNoLASGLG",text="FileNoLASGLG")
					self.Staff_table.heading("Bank",text="Bank")
					self.Staff_table.heading("Account",text="Account")
					self.Staff_table.heading("BVN",text="BVN")
					self.Staff_table.heading("Identity",text="Identity")
					self.Staff_table.heading("IdentifiedName",text="IdentifiedName")
					self.Staff_table.heading("Phone",text="Phone")
					self.Staff_table.heading("Address",text="Address")
					self.Staff_table.heading("PayStatus",text="PayStatus")
					self.Staff_table.heading("PayDate",text="PayDate")
					self.Staff_table.heading("Photo",text="Photo")
					self.Staff_table.heading("FromYear",text="From")
					self.Staff_table.heading("ToYear",text="To")
					self.Staff_table.heading("SecureCode",text="SecureCode")


					
					#Enable heading of tables to show
					self.Staff_table['show']='headings'
					
					#Set column width for each field in the table
					self.Staff_table.column("FormNo", anchor="center", width=120)
					self.Staff_table.column("LGAofRetire",width=120)
					self.Staff_table.column("FirstName",width=120)
					self.Staff_table.column("MiddleName",width=120)
					self.Staff_table.column("Surname",width=120)
					self.Staff_table.column("Gender", anchor="center", width=120)
					self.Staff_table.column("DateBirth", anchor="center", width=120)
					self.Staff_table.column("DateFAP", anchor="center", width=120)
					self.Staff_table.column("Rank",width=120)
					self.Staff_table.column("Grade", anchor="center", width=120)
					self.Staff_table.column("Step", anchor="center", width=120)
					self.Staff_table.column("DateRetire", anchor="center", width=120)
					self.Staff_table.column("CurrentStatus", anchor="center", width=120)
					self.Staff_table.column("DateDeath", anchor="center", width=120)
					self.Staff_table.column("State", anchor="center", width=120)
					self.Staff_table.column("LGAOrigin", anchor="center", width=120)
					self.Staff_table.column("Qualification", anchor="center", width=120)
					self.Staff_table.column("DateQual", anchor="center", width=120)
					self.Staff_table.column("SalaryPenMonth",  anchor="center",  width=120)
					self.Staff_table.column("GratuityBalance", anchor="center", width=120)
					self.Staff_table.column("PensionArrest", anchor="center", width=120)
					self.Staff_table.column("FileNoLASGLG",width=120)
					self.Staff_table.column("Bank", anchor="center", width=120)
					self.Staff_table.column("Account", anchor="center", width=120)
					self.Staff_table.column("BVN", anchor="center", width=120)
					self.Staff_table.column("Identity", anchor="center", width=120)
					self.Staff_table.column("IdentifiedName", anchor="center", width=120)
					self.Staff_table.column("Phone", anchor="center", width=120)
					self.Staff_table.column("Address",width=120)
					self.Staff_table.column("PayStatus", anchor="center", width=120)
					self.Staff_table.column("PayDate", anchor="center", width=120)
					self.Staff_table.column("Photo",width=150)
					self.Staff_table.column("FromYear",width=100)
					self.Staff_table.column("ToYear",width=100)
					self.Staff_table.column("SecureCode", anchor="center", width=150)

					#To expand the table  
					self.Staff_table.pack(fill=BOTH,expand=1)
					#Enable selection of items in the Bill_table
					self.Staff_table.bind("<ButtonRelease-1>",self.get_cursor)
					
					
					#=======================Bill Frame
					F3=LabelFrame(self.root,bd=10,relief=GROOVE)
					F3.place(x=950,y=485,width=395,height=185) 
					bill_title=Label(F3,text="Ticket",font="arial 15 bold",bd=5,relief=GROOVE).pack(fill=X)
					scroll_y=Scrollbar(F3,orient=VERTICAL)
					self.txtarea=Text(F3,yscrollcommand=scroll_y.set)
					scroll_y.pack(side=RIGHT,fill=Y)
					scroll_y.config(command=self.txtarea.yview)
					self.txtarea.pack(fill=BOTH,expand=1)		
					
					
					#=======================Bottom frame
					global Bottom_Frame
					Bottom_Frame=LabelFrame(self.root,bd=8,relief=GROOVE,bg=bg_color)
					Bottom_Frame.place(x=0,y=665,relwidth=1,height=45)
					
					SecureCode_txt=Entry(Bottom_Frame,textvariable=self.SecureCode,fg="White",bg="White",width=15,font=("Arial",10,"bold"),bd=5,relief=GROOVE,state='readonly')
					SecureCode_txt.grid(row=0,column=2,pady=0,padx=5,sticky="w")
					
					global From_txt
					From_lbl=Label(Bottom_Frame,text="From: ",bg=bg_color,fg="black",font=("times new roman",15,"bold")).grid(row=0,column=3,padx=5,pady=1,sticky="w")	
					From_txt=Entry(Bottom_Frame,width=15,textvariable=self.FromYear,font="arial 10 bold",bd=3,relief=SUNKEN)
					From_txt.grid(row=0,column=4,padx=5,pady=0,sticky="w")
					From_txt.focus()
					
					global To_txt
					To_lbl=Label(Bottom_Frame,text="To : ",bg=bg_color,fg="black",font=("times new roman",15,"bold")).grid(row=0,column=5,padx=5,pady=1,sticky="w")	
					To_txt=Entry(Bottom_Frame,width=15,textvariable=self.ToYear,font="arial 10 bold",bd=3,relief=SUNKEN)
					To_txt.grid(row=0,column=6,padx=5,pady=0,sticky="w")
					To_txt.focus()
					
					#Fetch data automatically
					self.fetch_data()
					self.Clear_data()
					self.ItemsInTreeView()
					
					#Directory for saving file to text
					global directory
					directory="C:/LGABills/"
					
					#Automatically runs the default of Welcome Bill
					self.Welcome_bill()
				
				def SaveCurrentTableItem(self):
					#Empty list for each column in the treeview
					column1_list = []
					column2_list = []
					column3_list = []
					column4_list = []
					column5_list = []
					column6_list = []
					column7_list = []
					column8_list = []
					column9_list = []
					column10_list = []
					column11_list = []
					column12_list = []
					column13_list = []
					column14_list = []
					column15_list = []
					column16_list = []
					column17_list = []
					column18_list = []
					column19_list = []
					column20_list = []
					column21_list = []
					column22_list = []
					column23_list = []
					column24_list = []
					column25_list = []
					column26_list = []
					column27_list = []
					column28_list = []
					column29_list = []
					column30_list = []
					column31_list = []
					column32_list = []
					column33_list = []
					column34_list = []
					column35_list = []
					
					#running through the lines of the treeview in a "for" function, append to each column list the value of the column in each line
					for child in self.Staff_table.get_children():
						column1_list.append(self.Staff_table.item(child)["values"][0]) 
						column2_list.append(self.Staff_table.item(child)["values"][1]) 
						column3_list.append(self.Staff_table.item(child)["values"][2]) 
						column4_list.append(self.Staff_table.item(child)["values"][3]) 
						column5_list.append(self.Staff_table.item(child)["values"][4]) 
						column6_list.append(self.Staff_table.item(child)["values"][5]) 
						column7_list.append(self.Staff_table.item(child)["values"][6]) 
						column8_list.append(self.Staff_table.item(child)["values"][7]) 
						column9_list.append(self.Staff_table.item(child)["values"][8]) 
						column10_list.append(self.Staff_table.item(child)["values"][9]) 
						column11_list.append(self.Staff_table.item(child)["values"][10]) 
						column12_list.append(self.Staff_table.item(child)["values"][11]) 
						column13_list.append(self.Staff_table.item(child)["values"][12]) 
						column14_list.append(self.Staff_table.item(child)["values"][13]) 
						column15_list.append(self.Staff_table.item(child)["values"][14]) 
						column16_list.append(self.Staff_table.item(child)["values"][15]) 
						column17_list.append(self.Staff_table.item(child)["values"][16]) 
						column18_list.append(self.Staff_table.item(child)["values"][17]) 
						column19_list.append(self.Staff_table.item(child)["values"][18]) 
						column20_list.append(self.Staff_table.item(child)["values"][19]) 
						column21_list.append(self.Staff_table.item(child)["values"][20]) 
						column22_list.append(self.Staff_table.item(child)["values"][21]) 
						column23_list.append(self.Staff_table.item(child)["values"][22]) 
						column24_list.append(self.Staff_table.item(child)["values"][23]) 
						column25_list.append(self.Staff_table.item(child)["values"][24]) 
						column26_list.append(self.Staff_table.item(child)["values"][25])
						column27_list.append(self.Staff_table.item(child)["values"][26])
						column28_list.append(self.Staff_table.item(child)["values"][27]) 
						column29_list.append(self.Staff_table.item(child)["values"][28]) 
						column30_list.append(self.Staff_table.item(child)["values"][29])
						column31_list.append(self.Staff_table.item(child)["values"][30])
						column32_list.append(self.Staff_table.item(child)["values"][31])
						column33_list.append(self.Staff_table.item(child)["values"][32])
						column34_list.append(self.Staff_table.item(child)["values"][33])
						column35_list.append(self.Staff_table.item(child)["values"][34])
					
					#create a dictionary from all the lists, using the header as the key and lists are the values as a list
					full_treeview_data_dict = {'FormNo': column1_list, 'LGAofRetire': column2_list, 'FirstName': column3_list, 'MiddleName': column4_list, 'Surname': column5_list, 'Gender': column6_list, 'DateBirth': column7_list, 'DateFAP': column8_list, 
												'Rank': column9_list, 'Grade': column10_list, 'Step': column11_list, 'DateRetire': column12_list, 'CurrentStatus': column13_list, 'DateDeath': column14_list, 'State': column15_list, 'LGAOrigin': column16_list,
												'Qualification': column17_list, 'DateQual': column18_list, 'SalaryPenMonth': column19_list, 'GratuityBalance': column20_list, 'PensionArrest': column21_list, 'FileNoLASGLG': column22_list, 
												'Bank': column23_list, 'Account': column24_list, 'BVN': column25_list,  'Identity': column26_list, 'IdentifiedName': column27_list, 'Phone': column28_list, 'Address': column29_list, 'PayStatus': column30_list, 'PayDate': column31_list, 'Photo': column32_list, 'From': column33_list, 'To': column34_list, 'SecureCode': column35_list,} 
												
					#Create a dataframe from the dictionary
					treeview_df = pd.DataFrame.from_dict(full_treeview_data_dict)
					
					#print(treeview_df)
					if len(mydata) < 1:
						messagebox.showerror("No Data","No data available to export")
						return False
					try:
						cwd='C:/'
						#filename = filedialog.asksaveasfilename(initialdir=os.getcwd(),title='Save to Excel',defaultextension='.xlsx',filetypes=[("Excel file", "*.xlsx")])
						filename = filedialog.asksaveasfilename(initialdir=cwd,title='Save to Excel',defaultextension='.xlsx',filetypes=[("Excel file", "*.xlsx")])
						treeview_df.to_excel(filename, engine='xlsxwriter',index= False)
						messagebox.showinfo("Data Exported","Your data has been exported to "+os.path.basename(filename)+" successfully.")
					except:
						pass
				
				#This function is used to search using keyword
				def search_data(self):
					try:
						#If one or both of the criteria is/are empty
						if self.search_by.get()=="" or self.search_txt.get()=="":
							messagebox.showerror("Search Error","Select Search by and \nType correct keyword")
						else:
							con=pymysql.connect(host="localhost",user="root",password="",database="lga")
							cur=con.cursor()
							cur.execute("select * from staff where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
							rows=cur.fetchall()
							if len(rows)!=0:
								self.Staff_table.delete(*self.Staff_table.get_children())
								for row in rows:
									self.Staff_table.insert('',END,values=row)
								con.commit()
							con.close()
							#Auto focus the last record from the records returned after search (highlight the first row automatically)
							child_id = self.Staff_table.get_children()[-1]
							cursor_row=self.Staff_table.focus(child_id)
							self.Staff_table.selection_set(child_id)
							self.get_cursor(cursor_row)
							self.ItemsInTreeView()
							
							
					except ValueError:
						messagebox.showerror("Data Search Error","You have made an invalid data search")
				
				def onClicked(self):
					try:
						#global cam, file, cv2, xyz
						cam = cv2.VideoCapture(0)
						count = 0
						#while True:
						if self.FormNo.get()=="" or self.LGAofRetire.get()=="":
							messagebox.showerror("Camera Error","Kindly make valid entry\nFormNo. and LGA of Retire are mandatory")
						else:
							while True:
								try:
									ret, img = cam.read()
									xyz = cv2.resize(img, (0,0), fx=0.32, fy=0.42)
									cv2.imshow("Press Space-Bar", xyz)
								except cv2.error:
									pass
								if not ret:
									break
									
								k=cv2.waitKey(1)
								
								if k%256==27:
									#For Esc Key
									#print("Close")
									try:
										cam.release()
										break
									except cv2.error:
										pass
								elif k%256==32:
									try:
										#For Space key
										#print("Image "+str(count)+"saved")
										file='C:/Images/'+str(self.FormNo.get())+'.jpg'
										cv2.imwrite(file, xyz)
										count += 1
									except cv2.error:
										pass
							self.OpenImageCam()	
						cam.release()
						cv2.destroyAllWindows()
					except Exception:
						pass
					
				def ClearCapturedClicked(self):
					try:
						for widget in passport_Frame.winfo_children():
							widget.destroy()
						self.photo_txt.set("****************AutoFill****************")
					except:
						pass
				
				#Function openfn for filedialog box that will enable opening of image files
				def openfn(self):
					global filename
					filename = filedialog.askopenfilename(initialdir='C:/',title='open',filetypes=[('jpg images','.jpg'),('png images','.png'),('gif images','.gif')])				
					return filename
					
				#This function OpenImage calls this function above for filename, resize the file, clear and add to the passport Frame				
				def OpenImage(self):
					x = self.openfn()
					#print (filename)
					img = Image.open(x)
					self.photo_txt.set(filename)
					img = img.resize((219, 235), Image.ANTIALIAS)
					img = ImageTk.PhotoImage(img)
					#To clear the passport frame
					for widget in passport_Frame.winfo_children():
						widget.destroy()
					#To add the image to the passport_Frame
					panel=Label(passport_Frame,image=img)
					panel.image=img
					panel.pack()
				
				#This function OpenImageCam automatically opens and display from Images folder the current image Captured from Cam
				#Using the filepath and filename FormNo
				def OpenImageCam(self):
					#x is default link to folder where all cam images will be saved
					x = 'C:/Images/'+str(self.FormNo.get())+'.jpg'
					self.photo_txt.set(x)
					img = Image.open(x)
					img = img.resize((219, 235), Image.ANTIALIAS)
					img = ImageTk.PhotoImage(img)
					#To clear the passport frame
					for widget in passport_Frame.winfo_children():
						widget.destroy()
					#To add the image to the passport_Frame
					panel=Label(passport_Frame,image=img)
					panel.image=img
					panel.pack()
					
				#Activate/Deactivate Date of Death depending on Status
				def getUpdateStatus(self, event):
					if self.CurrentStatus.get()=="DECEASED":
						DOD_txt.config(state=NORMAL)
						self.DOD.set("dd/mm/yyyy")
					else:
						DOD_txt.config(state=DISABLED)
						self.DOD.set("NIL")
				
				#Activate/Deactivate Name Identified depending on Identity
				def getUpdateIdentity(self, event):
					if self.Identity.get()=="SELF":
						self.IdentifiedName.set(str(self.FirstName.get())+" "+str(self.MiddleName.get())+" "+str(self.Surname.get()))
						IdentityKinName_txt.config(state=DISABLED)
					else:
						IdentityKinName_txt.config(state=NORMAL)
						self.IdentifiedName.set("")
				
				def getUpdateData(self,  event):
					#Once the Dept Combo value is changed this line will set the Unit Combo to empty
					combo_LGA.set("")
					#This line will display or populate the values of Unit under each category of active Dept
					combo_LGA['values'] = category[combo_State.get()]

				def get_cursor(self,ev):
					try:
						cursor_row=self.Staff_table.focus()
						contents=self.Staff_table.item(cursor_row)
						row=contents['values']
						self.FormNo.set(row[0])
						self.LGAofRetire.set(row[1])
						self.FirstName.set(row[2])
						self.MiddleName.set(row[3])
						self.Surname.set(row[4])
						self.Gender.set(row[5])
						self.DOB.set(row[6])
						self.DOofFAP.set(row[7])
						self.Rank.set(row[8])
						self.Grade.set(row[9])
						self.Step.set(row[10])
						self.DOR.set(row[11])
						self.CurrentStatus.set(row[12])
						self.DOD.set(row[13])
						self.State.set(row[14])
						self.LGA.set(row[15])
						self.Qualification.set(row[16])
						self.DOQ.set(row[17])
						self.SalaryPenMonth.set(row[18])
						self.GratuityBalance.set(row[19])
						self.PensionArrest.set(row[20])
						self.FileNoLASGLG.set(row[21])
						self.Bank.set(row[22])
						self.Account.set(row[23])
						self.BVN.set(row[24])
						self.Identity.set(row[25])
						self.IdentifiedName.set(row[26])
						self.Phone.set(str(0)+str(row[27]))
						self.Address.set(row[28])
						self.PayStatus.set(row[29])
						self.PayDate.set(row[30])
						self.photo_txt.set(row[31])
						self.FromYear.set(row[32])
						self.ToYear.set(row[33])
						self.SecureCode.set(row[34])
						
						#Bill Area
						self.prepare_bill()
						
					except:
						pass
					try:
						if self.photo_txt.get() == (""):
							#messagebox.showinfo('No Image!',"The Image file not added")
							for widget in passport_Frame.winfo_children():
								widget.destroy()
						else:
							x = self.photo_txt.get()
							img = Image.open(x)
							img = img.resize((219, 235), Image.ANTIALIAS)
							img = ImageTk.PhotoImage(img)
							#To clear the passport frame
							for widget in passport_Frame.winfo_children():
								widget.destroy()
							#To add the image to the passport_Frame
							panel=Label(passport_Frame,image=img)
							panel.image=img
							panel.pack()
					except:
						pass

				def prepare(self):
					##if self.FileNo_var.get()=="" or self.LGAofRetire.get()=="":
						##messagebox.showerror("Add Data Error","FileNo and Original Holder are mandatory")
					##else:
					self.mynice_date()                        
					global xz, randbillno
					randbillno=random.randint(1000,9999)
					#xz is the miscrosecond last part of datetime
					xz=str(datetime.now()).split('.')[1]
					#self.BillNo.set(str(randbillno)+x)			
						
						
						
				#NEW function to add info to DB
				def add_record(self):
					global y
					global z
					x=str()
					y=str()
					try:
						try:
							y=(int(self.Account.get()))
							z=(int(self.BVN.get()))						
						except ValueError:
							pass
						if self.FormNo.get()=="" or self.LGAofRetire.get()=="":
							messagebox.showerror("Add Data Error","Kindly make valid entry\nFormNo, LGA of Retire are mandatory")
						elif self.DOB.get()=="dd/mm/yyyy" or len((str(self.DOB.get()).split('/')[2]))!=4 or int((str(self.DOB.get()).split('/')[1]))>12:
							messagebox.showerror("Data Error","Date of Birth must be in dd/mm/yyyy format")
							DOB_txt.focus()
						elif self.DOofFAP.get()=="dd/mm/yyyy" or len((str(self.DOofFAP.get()).split('/')[2]))!=4 or int((str(self.DOofFAP.get()).split('/')[1]))>12:
							messagebox.showerror("Data Error","Date of 1st Appointment must be in dd/mm/yyyy format")
							DOofFAP_txt.focus()
						elif self.DOR.get()=="dd/mm/yyyy" or len((str(self.DOR.get()).split('/')[2]))!=4 or int((str(self.DOR.get()).split('/')[1]))>12:
							messagebox.showerror("Data Error","Date of Retire must be in dd/mm/yyyy format")
							DOR_txt.focus()
						elif self.CurrentStatus.get()=="DECEASED" and self.DOD.get()=="dd/mm/yyyy":
							messagebox.showerror("Data Error","Date of Death must be in dd/mm/yyyy format")
							DOD_txt.focus()
						elif self.DOQ.get()=="dd/mm/yyyy" or len((str(self.DOQ.get()).split('/')[2]))!=4 or int((str(self.DOQ.get()).split('/')[1]))>12:
							messagebox.showerror("Data Error","Date of Qualification must be in dd/mm/yyyy format")
							DOQ_txt.focus()
						elif len(self.Account.get()) != 10:
							messagebox.showerror("Add Data Error","Kindly make valid entry\nAccount Number is 10 digits & mandatory")
							Account_txt.focus()
						#elif (self.Account.get()) == "" or type(y)==str:
							#messagebox.showerror("Add Data Error","Kindly make valid entry\nAccount Number is 10 digits & mandatory\nIt cannot contain blanks or alphabets")
							#Account_txt.focus()
						elif len(self.BVN.get()) != 11:
							messagebox.showerror("Add Data Error","Kindly make valid entry\nBVN Number is 11 digits & mandatory")
							BVN_txt.focus()
						#elif (self.BVN.get()) == "" or type(z)==str:
							#messagebox.showerror("Add Data Error","Kindly make valid entry\nBVN Number is 11 digits & mandatory\nIt cannot contain blanks or alphabets")
							#BVN_txt.focus()
						elif self.IdentifiedName.get()=="":
							messagebox.showerror("Add Data Error","Kindly make valid entry\nIdentity/Kin & Identified Name are mandatory")
							combo_Identity.focus()
						elif self.photo_txt.get() == "****************AutoFill****************":
							messagebox.showerror("Add Data Error","Kindly make valid entry\nImage Passport is mandatory")
						##elif self.FromYear.get()=="":
							##messagebox.showerror("Add Data Error","Kindly make valid entry\nFrom Month.Year is mandatory")
							##From_txt.focus()
						##elif self.ToYear.get()=="":
							##messagebox.showerror("Add Data Error","Kindly make valid entry\nTo Month.Year is mandatory")
							##To_txt.focus()
						else:
							if self.Identity.get()=="SELF":
								self.IdentifiedName.set(str(self.FirstName.get())+" "+str(self.MiddleName.get())+" "+str(self.Surname.get()))
							self.prepare()
							self.PayDate.set(str(datetime.now()))
							self.SecureCode.set(str(randbillno)+xz)
							con=pymysql.connect(host="localhost",user="root",password="",database="lga")
							cur=con.cursor()
							cur.execute("insert into staff values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.FormNo.get(),
																																			self.LGAofRetire.get(),
																																			self.FirstName.get(),
																																			self.MiddleName.get(),
																																			self.Surname.get(),
																																			self.Gender.get(),
																																			self.DOB.get(),
																																			self.DOofFAP.get(),
																																			self.Rank.get(),
																																			self.Grade.get(),
																																			self.Step.get(),
																																			self.DOR.get(),
																																			self.CurrentStatus.get(),
																																			self.DOD.get(),
																																			self.State.get(),
																																			self.LGA.get(),
																																			self.Qualification.get(),
																																			self.DOQ.get(),
																																			self.SalaryPenMonth.get(),
																																			self.GratuityBalance.get(),
																																			self.PensionArrest.get(),
																																			self.FileNoLASGLG.get(),
																																			self.Bank.get(),
																																			self.Account.get(),
																																			self.BVN.get(),
																																			self.Identity.get(),
																																			self.IdentifiedName.get(),
																																			self.Phone.get(),
																																			self.Address.get(),
																																			self.PayStatus.get(),
																																			self.PayDate.get(),
																																			self.photo_txt.get(),
																																			self.FromYear.get(),
																																			self.ToYear.get(),
																																			self.SecureCode.get()
																																			))

							#Function of fetch_data is called here	
							con.commit()
							
							self.fetch_data()
						
							#Prepare Bill
							self.prepare_bill()
							
							#Automatically save bill as text file
							self.Save_bill()
							
							#Save to PDF with Image
							self.SaveTexttoPDF()
							
							#Function to clear the data after adding it to DB
							self.Clear_data()
							con.close()
							#Message box to indicate successfully added
							messagebox.showinfo('Successfully added!',"The record has been captured")
							self.ItemsInTreeView()	
							
							
						##except Exception:
							##messagebox.showerror("Add Data Error","There is a duplicate entry")
							
					except pymysql.err.IntegrityError or IndexError or TypeError:
						messagebox.showerror("Data Error","Form Number "+str(self.FormNo.get())+" already exists\nNo Duplicate is allowed.")
						
				#NEW Function to fetch data FOR TODAY
				def fetch_data(self):
					con=pymysql.connect(host="localhost",user="root",password="",database="lga")
					cur=con.cursor()
					#cur.execute("select * from packagerbills where
					#cur.execute("select * from staff where DateStamp LIKE '%"+str(datetime.now()).split(' ')[0]+"%'")
					cur.execute("select * from staff")
					rows=cur.fetchall()
					
					##NEWLY
					global mydata
					mydata=rows
					
					if len(rows)!=0:
						self.Staff_table.delete(*self.Staff_table.get_children())
						for row in rows:
							self.Staff_table.insert('',END,values=row)
						con.commit()
					#This function will Fetch the total sum of amount from the DB
					#self.DBTOTAL()
					con.close()
					
					self.ItemsInTreeView()
					#This function will clear the content of Sub-Total
					#self.SearchedSumation.set("")

				def UpdateDB_data(self):
					global y
					global z
					x=str()
					y=str()
					try:
						y=(int(self.Account.get()))
						z=(int(self.BVN.get()))						
					except ValueError:
						pass
					if self.FormNo.get()=="" or self.LGAofRetire.get()=="":
						messagebox.showerror("Update Error","Select record from table\n and Insert valid data")
					elif self.DOB.get()=="dd/mm/yyyy" or len((str(self.DOB.get()).split('/')[2]))!=4 or int((str(self.DOB.get()).split('/')[1]))>12:
						messagebox.showerror("Data Error","Date of Birth must be in dd/mm/yyyy format")
						DOB_txt.focus()
					elif self.DOofFAP.get()=="dd/mm/yyyy" or len((str(self.DOofFAP.get()).split('/')[2]))!=4 or int((str(self.DOofFAP.get()).split('/')[1]))>12:
						messagebox.showerror("Data Error","Date of 1st Appointment must be in dd/mm/yyyy format")
						DOofFAP_txt.focus()
					elif self.DOR.get()=="dd/mm/yyyy" or len((str(self.DOR.get()).split('/')[2]))!=4 or int((str(self.DOR.get()).split('/')[1]))>12:
						messagebox.showerror("Data Error","Date of Retire must be in dd/mm/yyyy format")
						DOR_txt.focus()
					elif self.CurrentStatus.get()=="DECEASED" and self.DOD.get()=="dd/mm/yyyy":
						messagebox.showerror("Data Error","Date of Death must be in dd/mm/yyyy format")
						DOD_txt.focus()		
					elif self.DOQ.get()=="dd/mm/yyyy" or len((str(self.DOQ.get()).split('/')[2]))!=4 or int((str(self.DOQ.get()).split('/')[1]))>12:
						messagebox.showerror("Data Error","Date of Qualification must be in dd/mm/yyyy format")
						DOQ_txt.focus()
					elif len(self.Account.get()) != 10:
						messagebox.showerror("Add Data Error","Kindly make valid entry\nAccount Number is 10 digits & mandatory")
						Account_txt.focus()
					##elif (self.Account.get()) == "" or type(y)==str:
						##messagebox.showerror("Add Data Error","Kindly make valid entry\nAccount Number is 10 digits & mandatory\nIt cannot contain blanks or alphabets")
						##Account_txt.focus()
					elif len(self.BVN.get()) != 11:
						messagebox.showerror("Add Data Error","Kindly make valid entry\nBVN Number is 11 digits & mandatory")
						BVN_txt.focus()
					##elif (self.BVN.get()) == "" or type(z)==str:
						##messagebox.showerror("Add Data Error","Kindly make valid entry\nBVN Number is 11 digits & mandatory\nIt cannot contain blanks or alphabets")
						##BVN_txt.focus()	
					elif self.IdentifiedName.get()=="":
						messagebox.showerror("Add Data Error","Kindly make valid entry\nIdentity/Kin & Identified Name are mandatory")		
					elif self.photo_txt.get() == "****************AutoFill****************":
						messagebox.showerror("Add Data Error","Kindly make valid entry\nImage Passport is mandatory")
					##elif self.FromYear.get()=="":
						##messagebox.showerror("Add Data Error","Kindly make valid entry\nFrom Month.Year is mandatory")
						##From_txt.focus()
					##elif self.ToYear.get()=="":
						##messagebox.showerror("Add Data Error","Kindly make valid entry\nTo Month.Year is mandatory")
						##To_txt.focus()	
					else:
						#Function to Update record on any selected entry
						ask=messagebox.askyesno("Update Record","Are you sure to proceed with update!")
						if ask==True:
							if self.Identity.get()=="SELF":
								self.IdentifiedName.set(str(self.FirstName.get())+" "+str(self.MiddleName.get())+" "+str(self.Surname.get()))
							con=pymysql.connect(host="localhost",user="root",password="",database="lga")
							cur=con.cursor()
							cur.execute("update staff set LGAofRetire=%s,FirstName=%s,MiddleName=%s,Surname=%s,Gender=%s,DateBirth=%s,DateFAP=%s,Rank=%s,Grade=%s,Step=%s,DateRetire=%s,CurrentStatus=%s,DateDeath=%s,State=%s,LGAOrigin=%s,Qualification=%s,DateQual=%s,SalaryPenMonth=%s,GratuityBalance=%s,PensionArrest=%s,FileNoLASGLG=%s,Bank=%s,Account=%s,BVN=%s,Identity=%s,IdentifiedName=%s,Phone=%s,Address=%s,PayStatus=%s,PayDate=%s,Photo=%s,FromYear=%s,ToYear=%s,SecureCode=%s where FormNo=%s",(
																																																																																	self.LGAofRetire.get(),
																																																																																	self.FirstName.get(),
																																																																																	self.MiddleName.get(),
																																																																																	self.Surname.get(),
																																																																																	self.Gender.get(),
																																																																																	self.DOB.get(),
																																																																																	self.DOofFAP.get(),
																																																																																	self.Rank.get(),
																																																																																	self.Grade.get(),
																																																																																	self.Step.get(),
																																																																																	self.DOR.get(),
																																																																																	self.CurrentStatus.get(),
																																																																																	self.DOD.get(),
																																																																																	self.State.get(),
																																																																																	self.LGA.get(),
																																																																																	self.Qualification.get(),
																																																																																	self.DOQ.get(),
																																																																																	self.SalaryPenMonth.get(),
																																																																																	self.GratuityBalance.get(),
																																																																																	self.PensionArrest.get(),
																																																																																	self.FileNoLASGLG.get(),
																																																																																	self.Bank.get(),
																																																																																	self.Account.get(),
																																																																																	self.BVN.get(),
																																																																																	self.Identity.get(),
																																																																																	self.IdentifiedName.get(),
																																																																																	self.Phone.get(),
																																																																																	self.Address.get(),
																																																																																	self.PayStatus.get(),
																																																																																	self.PayDate.get(),
																																																																																	self.photo_txt.get(),
																																																																																	self.FromYear.get(),
																																																																																	self.ToYear.get(),
																																																																																	self.SecureCode.get(),
																																																																																	self.FormNo.get()
																																																																																	))
							con.commit()
							#Function of fetch_data is called here
							self.fetch_data()
							#Display content of the Bill to enable saving into text file
							self.prepare_bill()
							#Automatically save bill as text file
							self.Save_bill()
							#Save to PDF with Image
							self.SaveTexttoPDF()
							#Function to clear the data from interface after Update to DB
							self.Clear_data()
							con.close()		
							self.ItemsInTreeView()
				
				#This function delete current selected record
				def delete_data(self):
					ask=messagebox.askyesno("Deleting Record","Are you sure to proceed with delete! \nYou cannot undo this action")
					if ask==True:
						con=pymysql.connect(host="localhost",user="root",password="",database="lga")
						cur=con.cursor()
						cur.execute("delete from staff where FormNo=%s",self.FormNo.get())
						con.commit()
						con.close()
						#Function of fetch_data is called here
						self.fetch_data()
						#Function to clear the data from interface after Delete from DB
						self.Clear_data()
						self.ItemsInTreeView()
				
				def Clear_data(self):
					#clear=messagebox.askyesno("Clear Data","Do you really want to Clear Screen?")
					#if clear>0:
					self.FormNo.set("")
					self.LGAofRetire.set("")
					self.FirstName.set("")
					self.MiddleName.set("")
					self.Surname.set("")
					self.Gender.set("")
					self.DOB.set("dd/mm/yyyy")
					self.DOofFAP.set("dd/mm/yyyy")
					self.Rank.set("")
					self.Grade.set("")
					self.Step.set("")
					self.DOR.set("dd/mm/yyyy")
					self.CurrentStatus.set("ALIVE")
					self.DOD.set("dd/mm/yyyy")		
					self.State.set("")
					self.LGA.set("")
					self.Qualification.set("")
					self.DOQ.set("dd/mm/yyyy")
					self.SalaryPenMonth.set("")
					self.GratuityBalance.set("")
					self.PensionArrest.set("")
					self.FileNoLASGLG.set("")
					self.Bank.set("")
					self.Account.set("")
					self.BVN.set("")
					self.Identity.set("")
					self.IdentifiedName.set("")
					self.Phone.set("")
					self.Address.set("")
					self.PayStatus.set("UNPAID")
					self.PayDate.set("****************AutoFill****************")
					self.search_by.set("")
					self.search_txt.set("")		
					self.photo_txt.set("****************AutoFill****************")
					self.SecureCode.set("")
					#Default VALUES
					self.FromYear.set("")
					self.ToYear.set("")
					
					FormNo_txt.focus()
					#Automatically show all DB in the Table and Disable Highlight from Table
					#Also disable selection of row from table
					self.fetch_data()
					self.Welcome_bill()
					for widget in passport_Frame.winfo_children():
						widget.destroy()
					
					self.ItemsInTreeView()
					
					IdentityKinName_txt.config(state=DISABLED)

				def ItemsInTreeView(self):
					global LabelDeaultPrinter
					counts=len(self.Staff_table.get_children())
					LabelDeaultPrinter=Label(Bottom_Frame,text=str("Number of Record(s): "+str(counts)),font="arial 10 bold",fg="Red").grid(row=0,column=0,padx=4,pady=4,sticky="w")
				
				#Function to display text in the Bill Area
				#Welcome Message constant displaying
				def Welcome_bill(self):
					self.txtarea.config(state=NORMAL)
					#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
					self.txtarea.delete('1.0',END)
					self.txtarea.insert(END,"  BORNO STATE COMMITTEE ON VERIFICATION OF\n")
					self.txtarea.insert(END,"LOCAL GOVT. PENSIONERS & PAYMENT OF GRATUITY\n")
					#self.txtarea.insert(END,"\t    (MAY.2012 - DEC.2012)")
					#self.txtarea.insert(END,"\n")
					self.txtarea.insert(END,"\n============================================")
					self.txtarea.config(state=DISABLED)
					#Function to input time frame in the Bill

				#Function to Modifying the format for DatePrepare and DatePaid
				def mynice_date(self):
					todaydate = datetime.now()                    
					lastpart=str(datetime.now()).split(' ')[1]
					new_today_date = todaydate.strftime("%d/%m/%Y")
					global today_date                    
					today_date = new_today_date+" "+lastpart                    
					return today_date	
					
					
				def prepare_bill(self):
					self.txtarea.config(state=NORMAL)
					#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
					self.txtarea.delete('1.0',END)
					self.txtarea.insert(END,"BORNO STATE COMMITTEE ON VERIFICATION OF\n")
					self.txtarea.insert(END,"LOCAL GOVT. PENSIONERS & PAYMENT OF GRATUITY\n")
					self.txtarea.insert(END,f"({self.FromYear.get()} - {self.ToYear.get()})")
					self.txtarea.insert(END,"\n============================================")
					#Function to input time frame in the Bill
					self.txtarea.insert(END,f"\nDate           : {self.PayDate.get()}")
					self.txtarea.insert(END,f"\nFile No.       : {self.FileNoLASGLG.get()}")
					#Adding more text with ability to capture Customer details
					self.txtarea.insert(END,f"\nForm Number    : {self.FormNo.get()}")
					self.txtarea.insert(END,f"\nRet.LGA        : {self.LGAofRetire.get()}")
					self.txtarea.insert(END,f"\nFullName       : {self.FirstName.get()} {self.MiddleName.get()} {self.Surname.get()}")
					self.txtarea.insert(END,f"\nGender         : {self.Gender.get()}")
					self.txtarea.insert(END,f"\nBirth          : {self.DOB.get()}")
					self.txtarea.insert(END,f"\nRank           : {self.Rank.get()}")
					self.txtarea.insert(END,f"\n1stAppnt       : {self.DOofFAP.get()}")
					self.txtarea.insert(END,f"\nGradeLevel     : {self.Grade.get()}")
					self.txtarea.insert(END,f"\nStep           : {self.Step.get()}")
					self.txtarea.insert(END,f"\nStatus         : {self.CurrentStatus.get()}")
					self.txtarea.insert(END,f"\nRetired        : {self.DOR.get()}")
					self.txtarea.insert(END,f"\nDeath Date     : {self.DOD.get()}")
					self.txtarea.insert(END,f"\nLGA Origin     : {self.LGA.get()}")
					self.txtarea.insert(END,f"\nState          : {self.State.get()}")
					self.txtarea.insert(END,f"\nQualificatn    : {self.Qualification.get()}")
					self.txtarea.insert(END,f"\nDateQual       : {self.DOQ.get()}")
					self.txtarea.insert(END,"\n============================================")
					self.txtarea.insert(END,f"\nSalPenMonth    : {self.SalaryPenMonth.get()}")
					self.txtarea.insert(END,f"\nBal.Gratuity   : {self.GratuityBalance.get()}")
					self.txtarea.insert(END,f"\nOuts.Pension   : {self.PensionArrest.get()}")
					self.txtarea.insert(END,"\n============================================")
					self.txtarea.insert(END,f"\nBank           : {self.Bank.get()}")
					self.txtarea.insert(END,f"\nAcc.No.        : {self.Account.get()}")
					self.txtarea.insert(END,f"\nBVN            : {self.BVN.get()}")
					self.txtarea.insert(END,"\n============================================")
					self.txtarea.insert(END,f"\nIdentiy/Kin    : {self.Identity.get()}")
					self.txtarea.insert(END,f"\nFullName       : {self.IdentifiedName.get()}")
					self.txtarea.insert(END,f"\nPhone          : {self.Phone.get()}")
					self.txtarea.insert(END,f"\nAddress        : {self.Address.get()}")
					self.txtarea.insert(END,f"\nPay Status     : {self.PayStatus.get()}")
					self.txtarea.insert(END,"\n============================================")
					self.mynice_date()
					self.txtarea.insert(END,f"\nSecure Code    : {self.SecureCode.get()}")
					self.txtarea.insert(END,f"\nDATE:__{str(today_date).split(' ')[0]}__  SIGN:_________________")
					self.txtarea.insert(END,"\n============================================")
					self.txtarea.config(state=DISABLED)
				
				def Save_bill(self):
					self.bill_data=self.txtarea.get('1.0',END)
					#print(self.bill_data)
					if not os.path.exists(directory):
						os.makedirs(directory)
					f1=open("C:/LGABills/"+str(self.FormNo.get())+".txt","w")
					f1.write(self.bill_data)
					f1.close()
				
				def SaveTexttoPDF(self):
					self.printout_bill()
					#Save FPDF() class into a variable pdf
					pdf = FPDF()
					#Add a page
					pdf.add_page()
					#Set font
					pdf.set_font("Arial", size=10)
					#Open the text file in read mode
					f=open("C:/LGABills/printout.txt","r")
					#Insert the texts in pdf
					for x in f:
						#5 is the line spacing, you can add or reduce it
						pdf.cell(200, 5, txt=x, ln=1, align = 'L')
					#save the pdf with name .pdf
					newpdf=(str(self.FormNo.get())+" "+str(self.SecureCode.get()))
					pdf.output("C:/LGABills/PDF/"+str(newpdf)+".pdf")
					
					global outputfile

					inputfile = ("C:/LGABills/PDF/"+newpdf+".pdf")
					outputfile =(str(self.FormNo.get())+" "+str(self.FirstName.get())+" "+str(self.MiddleName.get())+" "+str(self.Surname.get())+" "+str(self.SecureCode.get())+".pdf")
					piximage = str(self.photo_txt.get())

					#Define the position (upper right corner)
					image_rectangle = fitz.Rect(450,20,550,120)

					#retrieve the first page of the PDF
					file_handle = fitz.open(inputfile)
					first_page = file_handle[0]

					#add the image
					first_page.insertImage(image_rectangle, filename=piximage)

					#save the file
					file_handle.save("C:/LGABills/PDFnIMAGE/"+str(outputfile))
				
				def print_pdfbill(self):
					if self.FormNo.get()!="":
						#Save again
						self.SaveTexttoPDF()
						#Then Print pdf file
						#os.startfile("C:/LGABills/PDFnIMAGE/"+str(outputfile)+".pdf","print")
						os.startfile("C:/LGABills/PDFnIMAGE/"+str(outputfile),"print")
					else:
						messagebox.showerror("Print Error","Kindly select a Bill to print")
				
				def print_bill(self):
					if self.FormNo.get()!="":
						self.Save_bill()
						#Opens the main file using the Bill No.
						fin = open("C:/LGABills/"+str(self.FormNo.get())+".txt",'r')
						#print(fin)
						#Create another temporary file mainly for printing format
						fout = open("C:/LGABills/printout.txt","wt")
						#Condition statement for each line in the file main fin
						for line in fin:
							if line.startswith("Form Number"):
								fout.write(line.replace('		',''))
							elif line.startswith("Gender"):
								fout.write(line.replace('\t\t',''))
							elif line.startswith("GradeLevel"):
								fout.write(line.replace('\t\t',''))
							elif line.startswith("Status"):
								fout.write(line.replace('\t\t',''))
							elif line.startswith("Death Date"):
								fout.write(line.replace('\t\t',''))
							elif line.startswith("LGA Origin"):
								fout.write(line.replace('\t\t',''))	
							elif line.startswith("Qualificatn"):
								fout.write(line.replace('\t\t',''))
							elif line.startswith("Bank"):
								fout.write(line.replace('\t\t',''))
							elif line.startswith("Phone"):
								fout.write(line.replace('\t\t',''))	
							else:
								fout.write(line)	
						#Close the files
						fin.close()
						fout.close()
						os.startfile("C:/LGABills/printout.txt","print")
						#os.startfile(self.photo_txt.get(),"print")
					else:
						messagebox.showerror("Print Error","Kindly select a Bill to print")
					
				def printout_bill(self):
					if self.FormNo.get()!="":
						self.Save_bill()
						#Opens the main file using the Bill No.
						fin = open("C:/LGABills/"+str(self.FormNo.get())+".txt",'r')
						#print(fin)
						#Create another temporary file mainly for printing format
						fout = open("C:/LGABills/printout.txt","wt")
						#Condition statement for each line in the file main fin
						for line in fin:
							if line.startswith("Form Number"):
								fout.write(line.replace('		',''))
							elif line.startswith("Gender"):
								fout.write(line.replace('\t\t',''))
							elif line.startswith("GradeLevel"):
								fout.write(line.replace('\t\t',''))
							elif line.startswith("Status"):
								fout.write(line.replace('\t\t',''))
							elif line.startswith("Death Date"):
								fout.write(line.replace('\t\t',''))
							elif line.startswith("LGA Origin"):
								fout.write(line.replace('\t\t',''))	
							elif line.startswith("Qualificatn"):
								fout.write(line.replace('\t\t',''))
							elif line.startswith("Bank"):
								fout.write(line.replace('\t\t',''))
							elif line.startswith("Phone"):
								fout.write(line.replace('\t\t',''))	
							else:
								fout.write(line)	
						#Close the files
						fin.close()
						fout.close()	
				
			root=Tk()
			obj = BORNO_App(root)
			root.mainloop()

		else:
			messagebox.showerror("Invalid Login Details","Kindly Input Valid \nUsername and Password")
	except:
		#Quit the app due to lack of database communication
		exit()
		#messagebox.showerror("Invalid Login Details","Kindly Input Valid \nUsername and Password")
	
#Newly added
global master
master=Tk()
master.title("User Login")
w=400
h=380
ws = master.winfo_screenwidth()
hs = master.winfo_screenheight()
#calculate position x, y automatically base on the screen in use
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
master.geometry('%dx%d+%d+%d' % (w, h, x, y))
master.resizable(0,0)
master.configure(bg="DarkGray")

#Image for the background of Login Dialog
bg_icon=ImageTk.PhotoImage(file="images/bgnew.jpg")
bg_lbl=Label(master,image=bg_icon).pack()

#Image Logo on the login page
logoframe=Frame(master,bd=4,relief=RIDGE,bg="Gray")
logoframe.place(x=130,y=10,width=150,height=150)
logo=ImageTk.PhotoImage(file="images/logo.png")
logo_lbl=Label(logoframe,image=logo).pack()

#Label for the login dialog box
label=Label(master,text="VERIFICATION & GRATUITY",relief=GROOVE,font=("Arial",17,"bold"),fg="white",bg="green")
label.place(x=50,y=180)

#Making global variable of ery2 and ery3
global ery2,ery3,image

#Label to indicate instruction
label1=Label(master,text="Enter your login details",fg="Red",font=("Arial",12,"bold"))
label1.place(x=50,y=220)

#Username Label
label2=Label(master,text="UserName",relief=RIDGE,font=("Arial",10,"bold"),fg="Black")
label2.place(x=50,y=250)
#Text entry for Username
ery2=Entry(master,width=34)
ery2.place(x=150,y=250)
ery2.focus()

#Password Label
label2=Label(master,text="Password",relief=RIDGE,font=("Arial",10,"bold"),fg="Black")
label2.place(x=50,y=290)
#Text entry for Password
ery3=Entry(master,show="*",width=34,fg="Red")
ery3.place(x=150,y=290)

#Login Button
button1=Button(master,text="Login",font=("Arial",10,"bold"),command=user_valid,fg="Green")
button1.place(x=150,y=320)


#Quit Button
button3=Button(master,text="Quit ",font=("Arial",10,"bold"),command=login_quit,fg="Red")
button3.place(x=310,y=320)



master.mainloop()
			