function Disable-CurrentUser([String]$user)
{
    Disable-LocalUser -Name $user

    # Lock computer (Don't work from service)
    $xcmdString = {rundll32.exe user32.dll, LockWorkStation}
    Invoke-Command $xcmdString
}

Disable-CurrentUser -user $args[0]