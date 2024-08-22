*** Settings ***
Library    SeleniumLibrary
Library    Collections
Library    String
#Library    t2.py
Suite Setup    Open Browser and Maximize
Suite Teardown    Close Browse
#Test Setup
#Test Teardwon  

*** Variables ***
${from}  Coimbatore
${to}    Trivandrum
#${date}  21
${month}  August
${urlCustomer}    https://www.makemytrip.com/
${urlOperator}    https://www.operator.makemytrip.com

*** Test Cases ***
TC-001 Verify if a user is able to filter bus according to their preference
    
    Search Buses    ${from}    ${to}    ${month}      
    Select Filter    Travel Operators     A1 Travels
    Get All Bus Id   A1 Travels  Travel Operators
    Print Today's Date
    

*** Keywords ***

Open Browser and Maximize
    [Documentation]   Opening the browser and navigating into makemytrip link
    ...               clicking close button for the pop-up

    Open Browser     browser=chrome
    Maximize Browser Window
    Go To            https://www.makemytrip.com
    Sleep    5s
    Run Keyword And Ignore Error  Click Element    //span[@data-cy="closeModal"]

Search Buses
    [Documentation]  Searching the bus with From, To and Date conditions

    [Arguments]    ${fromCity}        ${toCity}    ${month}     ${date}=22

    Click Element    //nav//li[@class="menu_Buses"]
    Wait Until Element Is Visible     fromCity     10s
    Click Element        fromCity
    Wait Until Element Is Visible     //input[@placeholder="From"]     10s
    Input Text       //input[@placeholder="From"]     ${fromCity}
    Wait Until Element Is Visible    //div[contains(@class, 'autosuggest')]//span[contains(text(),'${fromCity},')]
    Click Element    //div[contains(@class, 'autosuggest')]//span[contains(text(),'${fromCity},')]

    Wait Until Element Is Visible     toCity     10s
    Run Keyword And Ignore Error        Click Element        toCity
    Wait Until Element Is Visible     //input[@placeholder="To"]     10s
    Input Text       //input[@placeholder="To"]     ${toCity}
    Wait Until Element Is Visible       //div[contains(@class, 'autosuggest')]//span[contains(text(),'${toCity},') or contains(text(),'(${toCity}),')]
    Click Element    //div[contains(@class, 'autosuggest')]//span[contains(text(),'${toCity},') or contains(text(),'(${toCity}),')]

    Run Keyword And Ignore Error    Click Element    travelDate      #date picker/calender will open up
    Wait Until Element Is Visible     //div[contains(text(), '${month}')]/ancestor::div[@class="DayPicker-Month"]//div[text()='${date}']     10s
    Click Element    //div[contains(text(), '${month}')]/ancestor::div[@class="DayPicker-Month"]//div[text()='${date}']
    Click Element    search_button 
    Wait Until Element Is Visible     //div[@class="busListingContainer"]//p[contains(text(),'found')]
 
Select Filter
    [Documentation]   Searching the filter "Travel Operator" and verifying its correct by taking count before and after applying the filter

    [Arguments]     ${filterType}     ${filterExactText}

    # take the initial count
    Click Element     toggle_buses
    ${initialCount}    Get Element Count     //div[@class="busCardContainer "]     # maximum bus in search result, no filter applied
    Click Element    //div[contains(text(),'${filterType}')]/../..//span[text()='${filterExactText}']
    Wait Until Element Is Not Visible     //div[@class="busListingContainer"]//p[contains(text(),'found') and contains(text(),'${initialCount}')]
    #wait till its not the previous count or wait till elemnt disappears.
    #[Setup]     Capture Page Screenshot

Get All Bus Id
    [Documentation]  Adding Travel Operator's name into a list and comparing them with selected filter name

    [Arguments]   ${BUS_NAME}    ${filterType}   

    [Setup]     Capture Page Screenshot
    @{allBusName}    Create List
    run keyword and ignore error     Click Element     //div[@id="toggle_buses" and not(contains(@class,'active'))]
    ${numberOfBuses}     Get Element Count    //div[starts-with(@id,"bus_")]//p[text()="${BUS_NAME}"]
    ${numberOfBuses}    Evaluate     $numberOfBuses+1
    FOR    ${index}    IN RANGE     1    ${numberOfBuses}
    ${busName}     Get Text      (//div[starts-with(@id,"bus_")]//p[text()="${BUS_NAME}"])[${index}]         # node with text in it, exact 3 matches.
    Append To List     ${allBusName}    ${busName}

    END
    Log    ${allBusName}

#Check Travel Operator


   FOR    ${i}    IN    @{allBusName}
    Run Keyword If       ${BUS_NAME}==${i}   fail
   END

    [Teardown]   click element  // div[text()="${filterType}"]/following-sibling::div[text()="CLEAR"]

#Print Today's Date
 #   [Documentation]    This test prints today's date in the log
  #  ${date}=    t2.Todays Date
   # Log    Today's date is: ${date}

Close Browse
    
    [Setup]     Capture Page Screenshot
    Close Browser

