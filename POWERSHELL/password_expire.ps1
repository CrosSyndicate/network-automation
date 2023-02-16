#attempting to make an interactable script using user input for the username to see days remaining until password expires - incomplete

$User = Read-Host -Prompt 'Input User Name'

#The string print below is to test if the variable above is being stored properly

[string]$User

function Get-PasswordExpiration($User){
    (([datetime]::FromFileTime((Get-ADUser -Identity $User -Properties "msDS-UserPasswordExpiryTimeComputed")."msDS-UserPasswordExpiryTimeComputed"))-(Get-Date)).Days
}

$Expiration = Get-PasswordExpiration($User)

Write-Output $Expiration

Read-Host -Prompt "Press Enter to Exit"