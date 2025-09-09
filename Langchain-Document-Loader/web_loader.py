from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()
parser = StrOutputParser()
template = PromptTemplate( 
    template='Answer the following question \n {question} from the following text - \n {text}',
    input_variables=['question','text'])




url = "https://www.amazon.in/KTM-Gunmetal-Metallic-Booking-Ex-Showroom/dp/B0F83362LK/?_encoding=UTF8&pd_rd_w=4x6Au&content-id=amzn1.sym.651c0a50-7c41-48d2-baa8-7e3e417543d4&pf_rd_p=651c0a50-7c41-48d2-baa8-7e3e417543d4&pf_rd_r=6C4BR9QW6F2E0D087XPS&pd_rd_wg=q4wgz&pd_rd_r=020e1086-8a4f-4630-8a8d-d1c65e9f6b3e&ref_=pd_hp_d_btf_ls_gwc_pc_en4_&th=1"


loader = WebBaseLoader(url)

docs = loader.load()

print(docs[0].page_content)


chain = template | model | parser

res = chain.invoke({"question" : "Whats the Post all about", 'text' : docs[0].page_content})

print("res is -> \n", res)




