import mysql.connector

def FeedbackUpdate(open_rating,open_feedback): 
              mydb = mysql.connector.connect(host="10.12.129.200", 
                                             user="mdevusr",  
                                             passwd="q4828uru99kk", 
                                             database="welc_dev") 
              mycursor = mydb.cursor() 
              sql='INSERT INTO digital_admin_feedback (rating, feedback) VALUES ("{0}","{1}");'.format(open_rating,open_feedback) 
              mycursor.execute(sql) 
              mydb.commit()
                      