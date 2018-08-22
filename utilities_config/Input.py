from selenium import webdriver

class InputParameter():


    #First Login Page Input

    login        ="LOG IN"
    login_username="username"
    login_password="password"
    username="mauli123"
    password="m@uli123"
    browser="chrome"
    url= "https://www.surveymonkey.com/"
    login_submit="//form[@id='sign_in_form']//button[@type='submit']"




    #Input For Create Intial Survey

    createsurvey="CREATE SURVEY"
    first_survey_title="surveyTitle"
    survey_send_key="Goverment"

    survey_selection="//div[@class='Select-placeholder']"
    survey_sel_final="//div[@id='react-select-2--option-0']"
    survey_sel_create="//button[@class='wds-button' and text()='CREATE SURVEY']"

    # Input for Start Survey

    entry = '//*[@id="scratch"]/span'
    createtitle = "title-text"
    surveyTitle = "//div[@id='surveyTitle']"
    new_survey_title = "Central Goverment"
    survey_save_final = "//*[@id='surveyTitleForm']//a[text()='SAVE']"
    page_title = "//span[text() = 'PAGE TITLE']"
    page_title_start = "//div[@id='pageTitle']"
    new_page_title = "New Page Title"
    page_title_save = "//*[@id='pageTitleForm']//a[text()='SAVE']"


    #Input For Asking  Question

    #Common paths

    question_typing="//div[@id='questionTitleWrap']//div[@id ='editTitle']"
    question_ans_patt="//a[@id='changeQType' and @class='sm-input']"
    question_save_butt="//div[@id='editQuestion']/section[@class='t1']//a[text()='SAVE']"








    #First Question:
    first_que_sendkey="Enter your email..?"
    first_que_ans_patt="//ul[@class='add-q-menu-left']//a[text()='Single Textbox']"




    #Second Question:
    second_que_sendkey="From when you are using Survey Monkey.?"
    second_que_ans_patt="//ul[@class='add-q-menu-right']//a[text()='Date / Time']"
    second_que_ans_patt2="//table[@id='rows']/tfoot[@class='answerTableFooter']//label[.='Time Info']"


    #Third Question:
    third_que_sendkey="How often do you use SurveyMonkey?"
    third_que_ans_patt="//ul[@class='add-q-menu-left']//a[text()='Multiple Choice']"
    third_que_sel="//div[@id='editQuestion']//select[@id='answerBankCategorySelect']"
    third_que_sel_specific="Always - Never"


    #Four Question:
    four_que_sendkey="How will rate the ease of survey creation?"
    four_que_ans_patt="//ul[@class='add-q-menu-left']//a[text()='Star Rating']"

    #Five Question:
    five_que_sendkey="Did you get meaningful data from survey analysis?"
    five_que_ans_patt="//ul[@class='add-q-menu-right']//a[text()='Dropdown']"

    five_que_sel="//div[@id='editQuestion']//select[@id='answerBankCategorySelect']"
    five_que_sel_specific="Yes - No"

    #Eight Question

    eight_que_sendkey="List the features you like most."
    eight_que_ans_patt="//ul[@class='add-q-menu-right']//a[text()='Multiple Textboxes']"

    eight_que_sel1="//table[@id='rows']/tbody[@class='answerSettingTextboxes']/tr[3]/td[1]/div/div[1]"
    eight_que_skey1="Question Bank"

    eight_que_sel2="//table[@id='rows']/tbody[@class='answerSettingTextboxes']/tr[4]/td[1]/div/div[1]"
    eight_que_skey2="Themes"

    eight_que_sel3="//table[@id='rows']/tbody[@class='answerSettingTextboxes']/tr[5]/td[1]/div/div[1]"
    eight_que_skey3="Graphical Result"

    eight_que_sel4="//table[@id='rows']/tbody[@class='answerSettingTextboxes']/tr[6]/td[1]/div/div[1]"
    eight_que_skey4="Template Re-usability"

    eight_que_sel5="//table[@id='rows']/tbody[@class='answerSettingTextboxes']/tr[7]/td[1]/div/div[1]"
    eight_que_skey5="Collectors"

    # Nine Question
    nine_que_sendkey="Will recommend SurveyMonkey to your friends / Colleagues?"
    nine_que_ans_patt="//ul[@class='add-q-menu-left']//a[text()='Multiple Choice']"
   # "//div[@id='editQuestion']//select[@id='answerBankCategorySelect']"

   #Ten Question
    ten_que_sendkey="Comments / Feedback (Text-area)"
    ten_que_ans_patt="//ul[@class='add-q-menu-left']//a[text()='Comment Box']"



