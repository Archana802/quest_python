*** Settings ***
Library    SeleniumLibrary
Library    Collections
Library    String
Library    t2.py

Suite Teardown   Print Today's Date
Test Teardown    Initial condition   Travel Operators

  

*** Variables ***
${fromCity}  Coimbatore
${toCity}    Trivandrum
#${month}  Aug
#${date}  23
${month}  August
${urlCustomer}    https://www.makemytrip.com/
${urlOperator}    https://www.operator.makemytrip.com


*** Test Cases ***
TC-001 Verify if a user is able to filter bus according to their preference

    Connect To Browser
    Enter MakeMyTrip Link
    Search Buses    ${fromCity}        ${toCity}     ${month}   23 Aug
    Select Filter    Travel Operators     A1 Travels
    Get filtered Bus Name    Travel Operators     A1 Travels


*** Keywords ***

Connect To Browser
    ${chrome_options}    Evaluate    sys.modules['selenium.webdriver'].ChromeOptions()    sys, selenium.webdriver
    ${dc}   Call Method     ${chrome_options}      to_capabilities
    Set To Dictionary    ${dc["goog:chromeOptions"]}    debuggerAddress    127.0.0.1:1111
    Create WebDriver    Chrome     alias=SFUI    options=${chrome_options}


Enter MakeMyTrip Link
    [Documentation]   Navigating into makemytrip link
    ...               clicking close button of the pop-up
        
    Go To            https://www.makemytrip.com
    Sleep    5s
    Run Keyword And Ignore Error  Click Element    //span[@data-cy="closeModal"]

Search Buses
    [Documentation]  Searching the bus with From, To and Date conditions

    [Arguments]    ${fromCity}        ${toCity}    ${month}     ${date}=Todays date

    ${date}    ${month}   Split String   ${date}    ${SPACE}

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
    ${dateLocator}  Set Variable If    ${date}=Todays
    ...     ////div[@aria-selected="true"]
    ...     //div[contains(text(), '${month}')]/ancestor::div[@class="DayPicker-Month"]//div[text()='${date}']
    Wait Until Element Is Visible     ${dateLocator}     10s
    Click Element    ${dateLocator}
    Click Element    search_button 
    Wait Until Element Is Visible     //div[@class="busListingContainer"]//p[contains(text(),'found')]

Select Filter
    [Documentation]   Searching the filter "Travel Operator" and verifying its correct by taking count before and after applying the filter

    [Arguments]     ${filterType}     ${filterExactText}

    
    Click Element     toggle_buses
    ${initialCount}    Get Element Count     //div[@class="busCardContainer "]     
    Click Element    //div[contains(text(),'${filterType}')]/../..//span[text()='${filterExactText}']
    Wait Until Element Is Not Visible     //div[@class="busListingContainer"]//p[contains(text(),'found') and contains(text(),'${initialCount}')]
    #[Setup]     Capture Page Screenshot

Get filtered Bus Name
    [Documentation]  Adding Travel Operator's name into a list and comparing them with selected filter name

    [Arguments]    ${filterType}   ${BUS_NAME}   

    @{allBusName}    Create List
    run keyword and ignore error     Click Element     //div[@id="toggle_buses" and not(contains(@class,'active'))]
    ${numberOfBuses}     Get Element Count    //div[starts-with(@id,"bus_")]//p[text()="${BUS_NAME}"]
    ${numberOfBuses}    Evaluate     $numberOfBuses+1
    FOR    ${index}    IN RANGE     1    ${numberOfBuses}
    ${busName}     Get Text      (//div[starts-with(@id,"bus_")]//p[text()="${BUS_NAME}"])[${index}]         # node with text in it, exact 3 matches.
    Append To List     ${allBusName}    ${busName}

    END
    Log    ${allBusName}
    
Verify Busname
    [Arguments]    ${filterType}   ${BUS_NAME} 

    Log    ${allBusName}

    FOR    ${i}    IN    @{allBusName}
    Should Be Equal As Strings     ${BUS_NAME}    ${i}
    END


Initial condition
    [Documentation]  Click on clear to undo my changes
    
    [Arguments]     ${filterType}

    #Click Element     //div[@class="filterContainer"]//p[text()="CLEAR ALL"]
    Click Element      //div[text()="${filterType}"]/following-sibling::div[text()="CLEAR"]




Print Today's Date
    [Documentation]    This test prints today's date in the log
    ${date}=    t2.Todays Date
    Log    Today's date is: ${date}    



    

