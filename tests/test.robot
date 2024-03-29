*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${BROWSER}  firefox
${URL}      http://localhost:5000

*** Test Cases ***
Example Test
    Open Browser  ${URL}  ${BROWSER}
    Page Should Contain Textfield    weight
    Click Element    weight
    Input Text    weight    150
    Page Should Contain Textfield    height
    Click Element    height
    Input Text    height    60
    Page Should Contain Button    Calculate BMI
    Click Button    Calculate BMI
    Page Should Contain    Obese
    Close Browser
