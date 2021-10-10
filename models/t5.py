from transformers import pipeline
import os



summarizer = pipeline("summarization")


os.environ["TOKENIZERS_PARALLELISM"] = "false"

ARTICLE =  '''

The Daman and Diu administration on Wednesday withdrew a circular that asked women staff to tie rakhis on male colleagues after the order triggered a backlash from employees and was ripped apart on social media.The union territory?s administration was forced to retreat within 24 hours of issuing the circular that made it compulsory for its staff to celebrate Rakshabandhan at workplace.?It has been decided to celebrate the festival of Rakshabandhan on August 7. In this connection, all offices/ departments shall remain open and celebrate the festival collectively at a suitable time wherein all the lady staff shall tie rakhis to their colleagues,? the order, issued on August 1 by Gurpreet Singh, deputy secretary (personnel), had said.To ensure that no one skipped office, an attendance report was to be sent to the government the next evening.The two notifications ? one mandating the celebration of Rakshabandhan (left) and the other withdrawing the mandate (right) ? were issued by the Daman and Diu administration a day apart. The circular was withdrawn through a one-line order issued late in the evening by the UT?s department of personnel and administrative reforms.?The circular is ridiculous. There are sensitivities involved. How can the government dictate who I should tie rakhi to? We should maintain the professionalism of a workplace? an official told Hindustan Times earlier in the day. She refused to be identified.The notice was issued on Daman and Diu administrator and former Gujarat home minister Praful Kodabhai Patel?s direction, sources said.Rakshabandhan, a celebration of the bond between brothers and sisters, is one of several Hindu festivities and rituals that are no longer confined of private, family affairs but have become tools to push politic al ideologies.In 2014, the year BJP stormed to power at the Centre, Rashtriya Swayamsevak Sangh (RSS) chief Mohan Bhagwat said the festival had ?national significance? and should be celebrated widely ?to protect Hindu culture and live by the values enshrined in it?. The RSS is the ideological parent of the ruling BJP.Last year, women ministers in the Modi government went to the border areas to celebrate the festival with soldiers. A year before, all cabinet ministers were asked to go to their constituencies for the festival.

'''
# ARTICLE = '''
# Kabul airport attack kills 60 Afghans, 13 US troops
# By SAYED ZIARMAL HASHEMI, RAHIM FAIEZ, LOLITA C. BALDOR and JOSEPH KRAUSS
# August 27, 2021
# Wounded Afghans lie on a bed at a hospital after a deadly explosions outside the airport in Kabul, Afghanistan, Thursday, Aug. 26, 2021. Two suicide bombers and gunmen attacked crowds of Afghans flocking to Kabul's airport Thursday, transforming a scene of desperation into one of horror in the waning days of an airlift for those fleeing the Taliban takeover. (AP Photo/Mohammad Asif Khan)
# 1 of 19
# Wounded Afghans lie on a bed at a hospital after a deadly explosions outside the airport in Kabul, Afghanistan, Thursday, Aug. 26, 2021. Two suicide bombers and gunmen attacked crowds of Afghans flocking to Kabul's airport Thursday, transforming a scene of desperation into one of horror in the waning days of an airlift for those fleeing the Taliban takeover. (AP Photo/Mohammad Asif Khan)
# KABUL, Afghanistan (AP) — Two suicide bombers and gunmen attacked crowds of Afghans flocking to Kabul’s airport Thursday, transforming a scene of desperation into one of horror in the waning days of an airlift for those fleeing the Taliban takeover. The attacks killed at least 60 Afghans and 13 U.S. troops, Afghan and U.S. officials said.

# The U.S. general overseeing the evacuation said the attacks would not stop the United States from evacuating Americans and others, and flights out were continuing. Gen. Frank McKenzie, head of U.S. Central Command, said there was a large amount of security at the airport, and alternate routes were being used to get evacuees in. About 5,000 people were awaiting flights on the airfield, McKenzie said.

# The blasts came hours after Western officials warned of a major attack, urging people to leave the airport. But that advice went largely unheeded by Afghans desperate to escape the country in the last few days of an American-led evacuation before the U.S. officially ends its 20-year presence on Aug. 31.

# The Islamic State group claimed responsibility for the killings on its Amaq news channel. The IS affiliate in Afghanistan is far more radical than the Taliban, who recently took control of the country in a lightning blitz. The Taliban were not believed to have been involved in the attacks and condemned the blasts.

# In an emotional speech from the White House, U.S. President Joe Biden said the latest bloodshed would not drive the U.S. out of Afghanistan earlier than scheduled, and that he had instructed the U.S. military to develop plans to strike IS.

# “We will not forgive. We will not forget. We will hunt you down and make you pay,” Biden said.

# U.S. officials initially said 11 Marines and one Navy medic were among those who died. Another service member died hours later. Eighteen service members were wounded and officials warned the toll could grow. More than 140 Afghans were wounded, an Afghan official said.

# One of the bombers struck people standing knee-deep in a wastewater canal under the sweltering sun, throwing bodies into the fetid water. Those who moments earlier had hoped to get on flights out could be seen carrying the wounded to ambulances in a daze, their own clothes darkened with blood.

# Emergency, an Italian charity that operates hospitals in Afghanistan, said it had received at least 60 patients wounded in the airport attack, in addition to 10 who were dead when they arrived.

# “Surgeons will be working into the night,” said Marco Puntin, the charity’s manager in Afghanistan. The wounded overflowed the triage zone into the physiotherapy area and more beds were being added, he said.

# The Afghan official who confirmed the overall Afghan toll spoke on condition of anonymity because he was not authorized to brief media.

# Pentagon spokesman John Kirby said one explosion was near an airport entrance and another was a short distance away by a hotel. McKenzie said clearly some failure at the airport allowed a suicide bomber to get so close to the gate.

# He said the Taliban has been screening people outside the gates, though there was no indication that the Taliban deliberately allowed Thursday’s attacks to happen. He said the U.S. has asked Taliban commanders to tighten security around the airport’s perimeter.

# Adam Khan was waiting nearby when he saw the first explosion outside what’s known as the Abbey gate.
# '''

print (summarizer(ARTICLE, max_length=130, min_length=60, do_sample=False))





