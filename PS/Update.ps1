$ServiceName = "PythonTaskSvc"
$NetEXE = $env:SystemDrive + "\windows\system32\net.exe"
$StopServiceCommand = $NetEXE + ' ' + "stop" + ' ' + $ServiceName
$StartServiceCommand = $NetEXE + ' ' + "start" + ' ' + $ServiceName

$GitHubSSH_Path = "git@github.com:pandrey76/WindowsRemoteManeger.git"

# Stoping service PythonTaskSvc
Invoke-Expression $StopServiceCommand


# Write-Host (Split-Path -Parent $PSCommandPath)

# Write-Host (Split-Path -Parent $PSCommandPath)

# Stoping service PythonTaskSvc
#Invoke-Expression $StartServiceCommand
#$StopDelay = Start-Sleep -Seconds 5
# Write-Host "Run after stop delay: " + $StopDelay.ToString()
#Write-Host $StopDelay
$CurrentScriptFolder = Split-Path -Parent $PSCommandPath
$UpFolder = "cd ..\"
# Write-Host($CD_Command)
# Write-Host($UpFolder)
#Invoke-Expression $CurrentScriptFolder
Invoke-Expression $UpFolder
# Invoke-Expression $CurrentScriptFolder
Invoke-Expression "git pull"
Invoke-Expression $StartServiceCommand

$GoToScriptFolder = "cd " + $CurrentScriptFolder
Invoke-Expression $GoToScriptFolder

# $StartDelay = Start-Sleep -Seconds 10
# Write-Host $StartDelay
# $NetEXE = $env:SystemDrive + "\windows\system32\net.exe localgroup administrators"
# $UserStringFromNetCommand = Invoke-Expression $NetEXE | Where {$_ -eq $UserNameSuffix}
#     if(!([String]::IsNullOrEmpty($UserStringFromNetCommand)))
#    {
#        throw $SCStringTable.ErrorUserNotFound
#    }