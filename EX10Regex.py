#Email Extracter
import re

str="""
Skip to content
Facebook-f
 Youtube
 Instagram
 Pinterest
National Genius Hunt
Research Journal
9888806027
9780040777
CONTACT
Rayat Bahra University
ABOUT
ADMISSION
ACADEMIC
EXAMINATION
INTERNATIONAL
RESEARCH
CAREER CENTER
CAMPUS LIFE
NIRF
Explore Rayat Bahra University
At Rayat Bahra University, we are committed to spirited learning, growth and professional development. We empower our students to ask insightful questions, explore disciplinary boundaries, and confront conventional ways of thinking. We invite you to learn more about Rayat Bahra University and discover an education built for you. 

Apply Now
700+
RESEARCH PUBLICATIONS

100+
RESEARCH FELLOW

1025+
RECRUITERS VISITED FOR PLACEMENTS

1 LAC +
ALUMNI

20+ LPA
HIGHEST PACKAGE OFFERED

10+ CR
WORTH SCHOLARSHIP AVAILABLE

150+ PROGRAMS
 






Approvals & Accreditations
Scholarship & Concessions
SC/ST SCHOLARSHIP AS PER GOVT. NORMS ( for Punjab, H.P., Chandigarh & Haryana)

90% TUTION FEE WAIVER
Merit Based scholarship

50% TUTITION FEE WAVER
Student whose both Parents/or father not alive

25% TUTION FEE WAIVER
Sibling Concession / Employee’s Ward – Concession / Alumni Concession

OUR PROUD ALUMNI
135915785_850763738825367_3606529493046753343_n.jpg
JAANI
India's number 1 songwriter and music composer

Abhijit Kaplish
ABHIJIT KAPLISH
IAS (All India RANK -15)

Madhavi
MADHAVI
PCS Officer

Gurjinder Singh
GURJINDER SINGH
1st Rank in JAG (All India Judge Advocate General)

Tarun Walia
TARUN WALIA
1st in HPJS (Himachal Pardesh Judical Services)

licensed-image
APARSHAKTI KHURANA
Bollywood actor, radio jockey, comedian, singer and television host.

OUR PROUD RBUians
 
NORTH INDIA'S LARGEST SKILL DEVELOPMENT CENTER
With it’s state of the art infrastructure, the Center provides constant access to skilled and dedicated faculty that uses innovative methods of teaching in imparting quality education to all. SDC has powerful tie-ups with the industry and has signed MOUs with several renowned corporate like Royal Enfield, Bosch, Eicher and many more.




ADMISSION OPEN 2022-23
APPLY NOW
INDUSTRIAL COLLABORATION
I8
I4
I6
I3
I7
I9
I2
I1
I5
T10
T11
T6 (2)
T9
T5
T7
T4
T3
T2
INTERNATIONAL TIE-UPS
Placements With Leading MNC's
 
Reliance Digital
ranbaxy-logo
hdfc-logo
godrej-logo
eicher-logo
denso-logo
amazon
Unisys
united health
Vivo
airtel
wipro
tvs
ITC
Mahindra
Tech_Mahindra
royal-enfield
havells
john-deere
nestle
zensar
icici
Sun pharma
abbott
Cipla
kpmg
capgemini
byjus
apollo
persistent
Oppo
sapient






MEMBERSHIPS & TRAINING PROGRAMS
2001
BE A PART OF THE UNPARALLELED LEGACY
APPLY NOW

Rayat Bahra group of Universities and Institutions has emerged as a premier destination of professional education in north India. The group is proud of its experienced faculty, energetic students, high achieving alumni, dedicated support staff and visionary management…

Read more
CONTACT INFO
RAYAT-BAHRA UNIVERSITY
Chandigarh-Ropar NH 205,
Greater Mohali, Punjab, INDIA - 140103

ADMISSION HELPLINE
98888-06027, 97800-40777

PHONE
0160-5009665, 0160-5009675

E-MAIL
info@rayatbahrauniversity.edu.in

ADMISSIONS
STUDY PROGRAMMES
APPLY NOW 2022
HOSTEL & MESS FEE
TRANSPORTATION FEE
BUS ROUTES
REFUND POLICY
BLOG
EXAMINATION
STAFF
EXAMINATION PROCESS
ACADEMIC RECORDS
GUIDELINES FOR ISSUE OF CEDRTIFICATES
Privacy Policy
Disclaimer
Facebook-f
 Youtube
 Instagram
 Pinterest
 Whatsapp
© 2022 Rayat Bahra University

Academic Records
Student Name

Roll Number

Contact Number

Email

Program Name

Year of Passing

Documents Required
Final DegreeProvisional DegreeDMCMigration CertificateOfficial Transcript

How to Receive Documents
On CampusNationwide DeliveryInternational Delivery

Mailing Address

Name

Address 1

Address 2

Address 3

City

State

Postal Code

Purpose of Request

   I accept terms & conditions


(AS PER ACADEMIC REGULATIONS & STUDENT CONDUCT RULES 2018, PAGE NO. 13)
The student has cleared all the courses prescribed for the program.
The student has obtained at the end of every semester SGPA of at least 4.5 for Diploma & under graduate courses and SGPA 5.0 for post graduate courses. (For M.Pharm, B.Pharm, D.Pharm, B.Pharm (Practice) Courses, SGPA will be 5.0).
The student has obtained a minimum CGPA of 5.00 for Diploma & under graduate courses and CGPA 5.5 for post graduate courses.
The student has not taken more time than specified for completion of the course.
Student has satisfied all the rules of evaluation.
No case of indiscipline or unfair means is pending against the student.
No dues are pending against the student.
Controller of Examination Department,
Academic Block, Rayat Bahra University,
Kharar, Mohali.(Punjab)
Phone No. 0160-5009665,75,71
Email: examination@rayatbahrauniversity.edu.in

Beneficiary Name: Controller of Examination Rayat Bahra University
Account No. 19341131000261
Bank Name: Punjab National Bank (e OBC)
IFSC CODE: ORBC0101934
Place: Sahauran (Mohali)

Academic documents requests are usually processed between one and three business days. During periods of high volume, it may take longer. All charges are nonrefundable. Document requests will not be processed for students with financial obligations to the university.

Hello! How can I help?
RBU Support

"""
email=re.findall(r"[0-9a-zA-Z._+%&]+@[0-9a-zA-Z._+%&]+[.][a-zA-Z.0-9]",str)
#email=re.findall(r'\W+@\S+\w',str)
print(email)