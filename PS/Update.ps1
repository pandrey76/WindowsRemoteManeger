$ServiceName = "PythonTaskSvc"
$NetEXE = $env:SystemDrive + "\windows\system32\net.exe"
$StopServiceCommand = $NetEXE + ' ' + "stop" + ' ' + $ServiceName
$StartServiceCommand = $NetEXE + ' ' + "start" + ' ' + $ServiceName

$GitHubSSH_Path = "git@github.com:pandrey76/WindowsRemoteManeger.git"
$LogFilePath = "c:/PS-Log.log"

# Stoping service PythonTaskSvc
######################################

# Invoke-Expression $StopServiceCommand
# Stop-Service -Name $ServiceName -Force

######################################

# Invoke delay
######################################

#Start-Sleep -Seconds 5

######################################


# Write-Host (Split-Path -Parent $PSCommandPath)

# Write-Host (Split-Path -Parent $PSCommandPath)

# Stoping service PythonTaskSvc
#Invoke-Expression $StartServiceCommand
#$StopDelay = Start-Sleep -Seconds 5
# Write-Host "Run after stop delay: " + $StopDelay.ToString()
#Write-Host $StopDelay
$CurrentScriptFolder = Split-Path -Parent $PSCommandPath
# Out-File -FilePath $LogFilePath -InputObject $CurrentScriptFolder -Append -Force


$UpFolder = "cd ..\"

# Write-Host($CD_Command)
# Write-Host($UpFolder)
#Invoke-Expression $CurrentScriptFolder
$GitRepoFolder = Split-Path -Path $CurrentScriptFolder -Parent
Set-Location $GitRepoFolder
# Invoke-Expression $UpFolder
Out-File -FilePath $LogFilePath -InputObject "############## git pull ##############" -Append -Force
Out-File -FilePath $LogFilePath -InputObject $GitRepoFolder -Append -Force
Out-File -FilePath $LogFilePath -InputObject "######################################" -Append -Force
# Invoke-Expression $CurrentScriptFolder

# git pull request
######################################

#Invoke-Expression "git pull"
Start-Process -FilePath "git.exe" -Args "remote show origin"  -RedirectStandardOutput "c:/PS-Output1.txt" -RedirectStandardError "C:/PS-Error1.txt"
Start-Process -FilePath "git.exe" -Args "pull -v"  -RedirectStandardOutput "c:/PS-Output.txt" -RedirectStandardError "C:/PS-Error.txt"
# -RedirectStandardInput "c:/Testsort.txt"

######################################

# Return to script folder
######################################

# $GoToScriptFolder = "cd " + $CurrentScriptFolder
# Invoke-Expression $GoToScriptFolder
Set-Location $CurrentScriptFolder

Out-File -FilePath $LogFilePath -InputObject $CurrentScriptFolder -Append -Force

######################################


# Restart Service
######################################

# Invoke-Expression $StartServiceCommand
Restart-Service -Name $ServiceName -Force
Out-File -FilePath $LogFilePath -InputObject "Restart Service $ServiceName" -Append -Force

######################################

# Start Service
######################################

# Invoke-Expression $StartServiceCommand
#Start-Service -Name $ServiceName -Force

######################################


# $StartDelay = Start-Sleep -Seconds 10
# Write-Host $StartDelay
# $NetEXE = $env:SystemDrive + "\windows\system32\net.exe localgroup administrators"
# $UserStringFromNetCommand = Invoke-Expression $NetEXE | Where {$_ -eq $UserNameSuffix}
#     if(!([String]::IsNullOrEmpty($UserStringFromNetCommand)))
#    {
#        throw $SCStringTable.ErrorUserNotFound
#    }