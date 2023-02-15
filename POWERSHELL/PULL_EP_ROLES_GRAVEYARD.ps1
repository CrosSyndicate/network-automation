$createdSinceDate = ((Get-Date).AddDays(-90)).Date

Get-ADUser -Filter {whenCreated -ge $createdSinceDate -and Name -notlike 's_*' -and Enabled -eq $True} -properties Name,City,Department,whenCreated | Select-Object -property Name,City,Department,whenCreated | Sort-Object -property Department -Descending | export-csv C:\Users\cgriffith\EP_users_2.csv

$date = (Get-Date).AddDays(-90).Date
Get-ADUser -Filter { WhenCreated -ge $date -and City -eq 'Fort Worth' -and Enabled -eq $True } `
  -Properties WhenCreated,City |
  Select-Object WhenCreated,City |
  export-csv C:\Users\cgriffith\EP_users_3.csv -NoTypeInformation



  Get-ADUser -Filter {Enabled -eq $True} -Property Created,LastLogonDate | Select-Object -Property Name, SAMAccountName, Created, LastLogonDate | export-csv C:\Users\cgriffith\EP_users.csv