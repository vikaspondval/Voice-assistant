import pyttsx3 as p
import speech_recognition as sr


engine = p.init()
rate = engine.getProperty("rate")
engine.setProperty("rate", 160)
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

r = sr.Recognizer()
speak("hello sir i'm your voice assistance. how may i help you?")
with sr.Microphone() as source:

    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source, 1.2)
    print("listening")
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text)

if "what" in text and "about" in text:
    speak("i am having a good day")
    speak("what can i do for you sir?")

if "are" in text and "you" in text:
    speak("I am voice assistant  and my name is disha bharti")

elif "who" in text and "creator" in text:
    speak("My creator is dev kapil and vikas")

elif "college" in text and "something" in text:
    speak(
        "DISHA BHARTI is the brain child of dedicated people known for their educational and social concerns. It caters to the long–felt academic need for having a professional institution in Saharanpur region."
    )

elif "it" in text and "affiliated" in text:
    speak(
        " It is affiliated to C.C.S. University under Self Finance it presents three undergraduate programs – BBA, BCA, B.Com. and a post graduate programme MBA affiliated to MTU, Noida (formerly known as UPTU)"
    )

elif "how" in text and "many" in text:
    speak(
        "there are seven courses and there names are Bachelor of Education, Mba, Bba, Bca, Bsc(c.s.), Ba and Bcom "
    )

elif "fee" in text and "Bachelor of Education" in text:
    speak(
        "FEE: First Year: Rupees Fifty one thousand two hundred fifty  , Second Year: Rupees Thirty thousand  , Duration: 2years(full time) and Eligibility: as per NCTE norms"
    )

elif "fee" in text and "MBA" in text:
    speak(
        "FEE: as per university , Duration: 2years(full time) and Eligibility: graduate with mimimum 50% marks"
    )

elif "fee" in text and "BBA" in text:
    speak(
        "FEE: 30,000 per year , Duration: 3years(full time) and Eligibility: graduate with mimimum 45% marks in 10 2"
    )

elif "fee" in text and "BCA" in text:
    speak(
        "FEE: as per university , Duration: 3years(full time) and Eligibility: graduate with mimimum 45% marks in 10 2"
    )

elif "fee" in text and "BSc(cs)" in text:
    speak(
        "FEE: 30,000 per year , Duration: 3years(full time) and Eligibility: graduate with mimimum 45% marks in 10 2(PCM)"
    )

elif "fee" in text and "Bcom" in text:
    speak(
        "FEE:As per merit , Duration: 3years(full time) and Eligibility: graduate with mimimum 33% marks in 10 2"
    )

elif "fee" in text and "BA" in text:
    speak(
        "FEE: As per merit , Duration: 3years(full time) and Eligibility: graduate with mimimum 33% marks in 10 2"
    )

elif "facilities" in text and "college" in text:
    speak(
        "Classrooms, Cafeteria, Computer Lab, Health Care Centre, Library, Seminar Hall, Sports Stadium are some facilites of our college "
    )

elif "faculty" in text and "details" in text:
    speak(
        " Head of Department (Commerce): Name:-Ranjana Rani, Designation:-Head of Department, Department:- Commerce, Qualification:-MCom, PhD, Work Experience:-18 years"
    )
    speak(
        " Name:-Sheetal Walia,   Designation:-Assistant Professor, Department:- IT,        Qualification:-MCA, PGDCA, M.A(Education),BSc,      Work Experience:-16  years"
    )
    speak(
        " Name:-Rajesh Saxena,   Designation:-Assistant Professor, Department:- IT,        Qualification:- MCA, M.Sc.,B.Ed,                    Work Experience:-12  years"
    )
    speak(
        " Name:-Shaifali Atray,  Designation:-Assistant Professor, Department:- Managment, Qualification:- PGDBM,M.Com,                        Work Experience:-8  years"
    )
    speak(
        " Name:-Shweta Mittal,   Designation:-Assistant Professor, Department:- IT,        Qualification:- MCA, B.Com,                         Work Experience:-7  years"
    )
    speak(
        " Name:-Ankur Sharma,    Designation:-Assistant Professor, Department:- Managment, Qualification:- UGC-NET, MBA, Pursuing Ph.D,        Work Experience:-8 years"
    )
    speak(
        " Name:-Nehal Jain,      Designation:-Assistant Professor, Department:- Managment, Qualification:-PGDBA, M.Com, B.Com,                 Work Experience:-7 years"
    )

elif "chair" in text and "person" in text:
    speak("The chairperson of disha bharti college is Mr Yashpal Bhatia")
    speak("Qualification: M.Phil., M.Sc. (Maths)")

elif "prin" in text and "cipal" in text:
    speak("The principal of disha bharti college is Dr. Kashi Ram Sharma")
    speak("Qualification: M.A., M.Sc. M.Ed., Ph.D")

elif "direc" in text and "tor" in text:
    speak("The director of disha bharti college is Mr gaurav aggarwal")

elif "whose" in text and "done" in text:
    speak("under the guidance of missus poonam tomar we have done this project")
    speak(
        "her qualification is -:she has done graduation in bsc, post graduation diploma in computer application, mca , she has cleared net exam and now she is pursuing phd."
    )
