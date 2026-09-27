import os
import pypdf
file_path=input("Enter the path of pdf file:").strip().strip("'\"")
if os.path.isdir(file_path):
    pdfs=sorted(f for f in os.listdir(file_path) if f.lower().endswith(".pdf"))
    for i,name in enumerate(pdfs,1):
        print(f"{i}. {name}")
    choice=int(input("Pick a file number: "))
    file_path=os.path.join(file_path,pdfs[choice-1])
def read_pdf(file_path):
    pdf=pypdf.PdfReader(file_path)
    text="\n".join(page.extract_text() for page in pdf.pages)
    return text
company=input("Enter company name: ")
dept=input("Enter department name: ")
import os
from openai import OpenAI
client=OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
def analyze_text(text):
    prompt=f"you are a career counselor.analyse the following text alias resume and provide the user with a detailed report including 1.Brief about the minimuum years of experience required by the company given by user.2.Suggest work shops and online short term courses to boost profile and highlight resume for that department of work(name real and well known ones)eg:coursera,udemy,edX.3. Specify and highlight the areas of interviews to be focused upn for better preperation eg:focusing on writing instant codes for simple day to day examples,presenting about yourself in a confident and structured manner . Give suggestions in a practical way and not as an ideal advice alone.\n\nCompany: {company}\nDepartment: {dept}\n\nResume:\n{text}"
    response=client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}],
        temperature=0.7
    )
    message=response.choices[0].message.content
    return message
result=analyze_text(read_pdf(file_path))
print(result)