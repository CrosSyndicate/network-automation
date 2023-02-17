#script has been edited to use generic username and domain names

$date = (Get-Date).AddDays(-90).Date
Get-ADUser -Filter { WhenCreated -ge $date -and City -eq 'Fort Worth' -and Enabled -eq $True } `
  -Properties WhenCreated,City |
  Select-Object WhenCreated,City |
  export-csv C:\Users\%USERNAME%\EP_users_3.csv -NoTypeInformation

###CODEGRAVE###

