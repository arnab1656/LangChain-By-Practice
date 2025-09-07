from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel, RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

model = ChatOpenAI()

class Review(BaseModel):

  sentiment:Literal["positive","negetive"] = Field(description='Give the sentiment of the feedback')   

parser =  StrOutputParser()
parser_pydantic = PydanticOutputParser(pydantic_object = Review)

prompt_for_check = PromptTemplate(
    template='Classify the sentiment of the following feedback text into postive or negative \n {feedback} \n {format_instruction}',
    input_variables=['feedback'],
    partial_variables={'format_instruction':parser_pydantic.get_format_instructions()}
)

classifier_chain = prompt_for_check | model | parser_pydantic

prompt_for_pos = PromptTemplate(
    template='Write an appropriate response to this positive feedback \n {feedback}',
    input_variables=['feedback']
)

prompt_for_neg = PromptTemplate(
    template='Write an appropriate response to this positive feedback \n {feedback}',
    input_variables=['feedback']
)

branch_chain = RunnableBranch(
    (lambda x : x.sentiment == "positive", prompt_for_pos | model | parser ),
    (lambda x : x.sentiment == "negetive", prompt_for_neg | model | parser ),
    (RunnableLambda(lambda x : "Cannot find Appropriate Feedback"))
)


review = """ 
Introduction
The Aurora X10 is the latest flagship from Aurora Mobile, aiming to strike a balance between raw performance, elegant design, and meaningful everyday features. After using it extensively for two weeks as my primary device, here’s a deep dive into what works, what doesn’t, and whether it deserves a place in your pocket.

Design & Build
Aurora continues to refine its design language. The X10 features a frosted glass back with a subtle gradient that plays with light without screaming for attention. The aluminum frame is solid, offering a reassuring heft at 195g — not too heavy, not feather-light. The curved edges are comfortable, though some may prefer the flat-sided trend. IP68 water and dust resistance are present, giving peace of mind for everyday accidents.

Display
This is where the X10 shines — literally. The 6.7-inch AMOLED panel boasts a QHD+ resolution, 120Hz refresh rate, and peak brightness of 2,500 nits. HDR10+ content looks stunning, colors are punchy without being oversaturated, and outdoor visibility is exceptional. The adaptive refresh rate smartly scales between 1Hz and 120Hz, saving battery when viewing static content.

Performance
Under the hood, the Aurora X10 runs on the Snapdragon 8 Gen 4 with 12GB of LPDDR5X RAM. It handles everything you throw at it — from intense gaming sessions to multitasking between heavy productivity apps — without breaking a sweat. Thermal management is improved, with less throttling under sustained loads compared to last year’s model. UFS 4.0 storage keeps read/write speeds blazing fast.

Software Experience
Running AuroraOS 14 on top of Android 15, the software feels fluid, clean, and modern. Aurora has reduced bloatware significantly, with only a handful of removable pre-installed apps. Updates are promised for five years — three major Android versions and two years of security patches beyond that. Multitasking gestures, a refined always-on display, and smart widgets add subtle yet useful touches.

Cameras
The camera system comprises a 50MP main sensor with OIS, a 48MP ultrawide, and a 10MP 5x telephoto lens. Photos in daylight are detailed and vibrant, with natural color reproduction. Low-light performance is impressive, thanks to a wider aperture and improved computational photography. The telephoto lens delivers sharp results, though dynamic range can occasionally falter in challenging lighting. Video recording supports up to 8K30 and 4K60 with solid stabilization.

Battery Life & Charging
A 5,000mAh battery powers the X10, easily lasting a full day of heavy use or two days of moderate use. The combination of efficient hardware and smart software optimizations delivers consistently good endurance. Wired charging at 65W tops the phone from 0 to 80% in about 25 minutes, while 30W wireless charging is convenient for desk setups. Reverse wireless charging is supported at 10W for accessories.

Audio & Connectivity
Stereo speakers tuned for Dolby Atmos output loud, balanced sound, with noticeable bass presence for a phone. The in-display fingerprint scanner is fast and accurate, and face unlock is improved with better low-light detection. Connectivity-wise, the X10 supports Wi-Fi 7, Bluetooth 5.4, and global 5G bands — future-proofed for the next few years.
"""

mainChain = classifier_chain | branch_chain

res = mainChain.invoke({"feedback" : review })


print("res --> \n",res)

mainChain.get_graph().print_ascii()

