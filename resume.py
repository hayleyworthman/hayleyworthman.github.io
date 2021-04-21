Contact_Hayley = {"Name": "Hayley Worthman",
                   "Location": '42.11321718026631, -71.16997527334297',
                   "Phone": "339.237.0891",
                   "Email": 'mailto:worthman.hayley@gmail.com',
                   "LinkedIn:": 'http://linkedin.com/in/hayleyworthman',
                   "GitHub": 'http://github.com/hayleyworthman'}

Education = {"Masters Degree": "New Mexico State University",
              "Masters in": "Communication Studies",
              "Graduated with": "4.0 GPA",
              "Undergrad Degree": "University of Massachusetts, Amherst",
              "Bachelors in": "Psychology",
              "Masters graduation year": "2012",
              "Bachelors graduation year": "2008"}

Programming_Skills = {"Python": "Hayley built me using Python!",
                      "HTML": "Basic",
                      "CSS": "Intermediate",
                      "PHP": "Basic",
                      "ParseHub": "Basic"}

#Web dev projects
WordPress_Sites = {"Book Signing Events": 'https://booksigningevent.com/',
                       "#1 Job Fair Calendar Site on Google": 'https://jobfairsin.com'},
Bravenet_Sites = {"Boston Convention Center Hotel Guide": 'https://bostonconventioncenter.com'}
Wix = {"Pranava Yoga Studio": 'https://www.pranavayoga.studio/',
       "Caregivers of Alzheimer's & Dementia Retreat": 'https://www.caregiverwellnessretreat.com/',
       "Dr. Patricia Van Tosh": 'https://www.drvantosh.com/'}

Technical_Skills = {"Web Development": [WordPress_Sites,
                                        Bravenet_Sites,
                                        Wix,],
                    "MySQL": "Basic",
                    "GitHub": 'http://github.com/hayleyworthman',
                    "Slack": "",
                    "MailChimp": "Digital and graphic design, automation, content curation, analytics",
                    "OntraPort": "62k+ subscriber lists, drip campaigns, nurture emails, track and analyze to optimize lead growth",
                    "Google Tools": ["Google Search Console", "Google Analytics", "Google AdSense", "Google Markup", "Google Ads"],
                    "LeadPages": "Designed registration and info pages for user friendly experience",
                    "Zapier": "Zap Dev, Zapier API automation for several apps",
                    "Canva": {"10 Ways to Master the Art of Class Theming with Sianna Sherman": 'http://bit.ly/SiannaSherman-Lead-Magnet',
                              "Premier Virtual Webinar Promo Banners": 'http://bit.ly/Premier-Virtual-Webinar-Promos',
                              "ZipRecruiter Desktop Pop Up":'http://bit.ly/Pop-Up-ZipRecruiter',
                              "Pine Realty Rental Sign": 'http://bit.ly/Pine-Realty',
                              "Caregiver Wellness Retreat Banner":'http://bit.ly/Caregiver-Santa-Fe-Retreat-Banner'}
                    }

for resume_highlights in Contact_Hayley:
    print(Contact_Hayley[resume_highlights])

for resume_highlights in sorted(list(Education.keys())):
    print(resume_highlights + " - " + Education[resume_highlights])

#make technical skills a list
tech_list = list(Technical_Skills.items())
print(tech_list)

for details in tech_list:
    skill, details = details
    print(skill + " experience = " + details)

print(dict(tech_list))
