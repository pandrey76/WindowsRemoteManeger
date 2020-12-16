$ServiceName = "PythonTaskSvc"
$NetEXE = $env:SystemDrive + "\windows\system32\net.exe"
$StopServiceCommand = $NetEXE + ' ' + "stop" + ' ' + $ServiceName
$StartServiceCommand = $NetEXE + ' ' + "start" + ' ' + $ServiceName

$GitHubSSH_Path = "git@github.com:pandrey76/WindowsRemoteManeger.git"
$LogFilePath = "c:/PS-Log.log"
$ActionStatusFile = "c:/PS-ActionStatus.txt"

$OutputStreamFile = "c:/PS-Output.txt"
$InputStreamFile =  "c:/PS-Input.txt"
$ErrorStreamFile = "c:/PS-Error.txt"
$Splitter = "######################################"
$ErrorSplitter = "**************************************"

New-Item -ItemType File -Path $ActionStatusFile -Force
if ($Error) {

    Add-Content -Path $ActionStatusFile -Value $PSErrorPresentString -Force
    Add-Content -Path $ActionStatusFile -Value $ErrorSplitter -Force
    Add-Content -Path $ActionStatusFile -Value ($Error[0].ToString() + $Error[0].InvocationInfo.PositionMessage) -Force
    Add-Content -Path $ActionStatusFile -Value $ErrorSplitter -Force
    Add-Content -Path $ActionStatusFile -Value "" -Force
    Add-Content -Path $ActionStatusFile -Value "" -Force
    $Error.Clear()
}

$RunCommand = "git.exe"
$ArgsForGettingRemoteRepoInfo = "remote show origin"
$ArgsForRunningPullCommand = "pull -v"
$ArgsForGettingLastRepoCommit = "log --name-status HEAD^..HEAD"

$PSErrorPresentString = "PS return error"
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

# Get current time
######################################
$Error.Clear()
$TempTime = Get-Date
if ($Error) {

    Add-Content -Path $ActionStatusFile -Value $PSErrorPresentString -Force
    Add-Content -Path $ActionStatusFile -Value $ErrorSplitter -Force
    Add-Content -Path $ActionStatusFile -Value ($Error[0].ToString() + $Error[0].InvocationInfo.PositionMessage) -Force
    Add-Content -Path $ActionStatusFile -Value $ErrorSplitter -Force
    Add-Content -Path $ActionStatusFile -Value "" -Force
    Add-Content -Path $ActionStatusFile -Value "" -Force
    $Error.Clear()
}
Add-Content -Path $ActionStatusFile -Value "Current service time" -Force
Add-Content -Path $ActionStatusFile -Value $Splitter -Force
Add-Content -Path $ActionStatusFile -Value $TempTime -Force
Add-Content -Path $ActionStatusFile -Value $Splitter -Force
# Get current script folder
######################################


$CurrentScriptFolder = Split-Path -Parent $PSCommandPath
if ($Error) {

    Add-Content -Path $ActionStatusFile -Value $PSErrorPresentString -Force
    Add-Content -Path $ActionStatusFile -Value $ErrorSplitter -Force
    Add-Content -Path $ActionStatusFile -Value ($Error[0].ToString() + $Error[0].InvocationInfo.PositionMessage) -Force
    Add-Content -Path $ActionStatusFile -Value $ErrorSplitter -Force
    Add-Content -Path $ActionStatusFile -Value "" -Force
    Add-Content -Path $ActionStatusFile -Value "" -Force
    $Error.Clear()
}
######################################

# Out-File -FilePath $LogFilePath -InputObject $CurrentScriptFolder -Append -Force

$UpFolder = "cd ..\"

# Write-Host($CD_Command)
# Write-Host($UpFolder)
#Invoke-Expression $CurrentScriptFolder

# Go to project folder
######################################

$GitRepoFolder = Split-Path -Path $CurrentScriptFolder -Parent
if ($Error) {

    Add-Content -Path $ActionStatusFile -Value $PSErrorPresentString -Force
    Add-Content -Path $ActionStatusFile -Value $ErrorSplitter -Force
    Add-Content -Path $ActionStatusFile -Value ($Error[0].ToString() + $Error[0].InvocationInfo.PositionMessage) -Force
    Add-Content -Path $ActionStatusFile -Value $ErrorSplitter -Force
    Add-Content -Path $ActionStatusFile -Value "" -Force
    Add-Content -Path $ActionStatusFile -Value "" -Force
    $Error.Clear()
}

Set-Location $GitRepoFolder
if ($Error) {

    Add-Content -Path $ActionStatusFile -Value $PSErrorPresentString -Force
    Add-Content -Path $ActionStatusFile -Value $ErrorSplitter -Force
    Add-Content -Path $ActionStatusFile -Value ($Error[0].ToString() + $Error[0].InvocationInfo.PositionMessage) -Force
    Add-Content -Path $ActionStatusFile -Value $ErrorSplitter -Force
    Add-Content -Path $ActionStatusFile -Value "" -Force
    Add-Content -Path $ActionStatusFile -Value "" -Force
    $Error.Clear()
}
$TempCurrentFolder = (Get-Location).Path
if ($Error) {

    Add-Content -Path $ActionStatusFile -Value $PSErrorPresentString -Force
    Add-Content -Path $ActionStatusFile -Value $ErrorSplitter -Force
    Add-Content -Path $ActionStatusFile -Value ($Error[0].ToString() + $Error[0].InvocationInfo.PositionMessage) -Force
    Add-Content -Path $ActionStatusFile -Value $ErrorSplitter -Force
    Add-Content -Path $ActionStatusFile -Value "" -Force
    Add-Content -Path $ActionStatusFile -Value "" -Force
    $Error.Clear()
}
# Logging

Add-Content -Path $ActionStatusFile -Value "Go to project folder" -Force
Add-Content -Path $ActionStatusFile -Value $Splitter -Force
Add-Content -Path $ActionStatusFile -Value $TempCurrentFolder -Force
$TempString = (Get-ChildItem -Path $TempCurrentFolder | Out-String)
if ($Error) {

    Add-Content -Path $ActionStatusFile -Value $PSErrorPresentString -Force
    Add-Content -Path $ActionStatusFile -Value $ErrorSplitter -Force
    Add-Content -Path $ActionStatusFile -Value ($Error[0].ToString() + $Error[0].InvocationInfo.PositionMessage) -Force
    Add-Content -Path $ActionStatusFile -Value $ErrorSplitter -Force
    Add-Content -Path $ActionStatusFile -Value "" -Force
    Add-Content -Path $ActionStatusFile -Value "" -Force
    $Error.Clear()
}
Add-Content -Path $ActionStatusFile -Value $TempString -Force
Add-Content -Path $ActionStatusFile -Value $Splitter -Force
Add-Content -Path $ActionStatusFile -Value "" -Force
Add-Content -Path $ActionStatusFile -Value "" -Force

######################################

# Get git repo info
######################################

Add-Content -Path $ActionStatusFile -Value "Getting git repo info" -Force
Add-Content -Path $ActionStatusFile -Value $Splitter -Force
Add-Content -Path $ActionStatusFile -Value "Running command" -Force
$FullRunningCommand = "Start-Process -FilePath $RunCommand -Args $ArgsForGettingRemoteRepoInfo  -RedirectStandardOutput $OutputStreamFile -RedirectStandardError $ErrorStreamFile"
Add-Content -Path $ActionStatusFile -Value $FullRunningCommand -Force

#Invoke-Expression $FullRunningCommand
Start-Process -FilePath $RunCommand -Args $ArgsForGettingRemoteRepoInfo  -RedirectStandardOutput $OutputStreamFile -RedirectStandardError $ErrorStreamFile -Wait
if ($Error) {

    Add-Content -Path $ActionStatusFile -Value $PSErrorPresentString -Force
    Add-Content -Path $ActionStatusFile -Value $ErrorSplitter -Force
    Add-Content -Path $ActionStatusFile -Value ($Error[0].ToString() + $Error[0].InvocationInfo.PositionMessage) -Force
    Add-Content -Path $ActionStatusFile -Value $ErrorSplitter -Force
    Add-Content -Path $ActionStatusFile -Value "" -Force
    Add-Content -Path $ActionStatusFile -Value "" -Force
    $Error.Clear()
}

$TempOutPutContent = (Get-Content -Path $OutputStreamFile | Out-String)
if ($Error) {

    Add-Content -Path $ActionStatusFile -Value $PSErrorPresentString -Force
    Add-Content -Path $ActionStatusFile -Value $ErrorSplitter -Force
    Add-Content -Path $ActionStatusFile -Value ($Error[0].ToString() + $Error[0].InvocationInfo.PositionMessage) -Force
    Add-Content -Path $ActionStatusFile -Value $ErrorSplitter -Force
    Add-Content -Path $ActionStatusFile -Value "" -Force
    Add-Content -Path $ActionStatusFile -Value "" -Force
    $Error.Clear()
}

Add-Content -Path $ActionStatusFile -Value "Output content" -Force
Add-Content -Path $ActionStatusFile -Value $TempOutPutContent -Force

$TempErrorContent = (Get-Content -Path $ErrorStreamFile | Out-String)
if ($Error) {

    Add-Content -Path $ActionStatusFile -Value $PSErrorPresentString -Force
    Add-Content -Path $ActionStatusFile -Value $ErrorSplitter -Force
    Add-Content -Path $ActionStatusFile -Value ($Error[0].ToString() + $Error[0].InvocationInfo.PositionMessage) -Force
    Add-Content -Path $ActionStatusFile -Value $ErrorSplitter -Force
    Add-Content -Path $ActionStatusFile -Value "" -Force
    Add-Content -Path $ActionStatusFile -Value "" -Force
    $Error.Clear()
}

Add-Content -Path $ActionStatusFile -Value "Error content" -Force
Add-Content -Path $ActionStatusFile -Value $TempErrorContent -Force
Add-Content -Path $ActionStatusFile -Value $Splitter -Force
Add-Content -Path $ActionStatusFile -Value "" -Force
Add-Content -Path $ActionStatusFile -Value "" -Force

######################################

# Invoke-Expression $UpFolder
# Out-File -FilePath $LogFilePath -InputObject "############## git pull ##############" -Append -Force
# Out-File -FilePath $LogFilePath -InputObject $GitRepoFolder -Append -Force
# Out-File -FilePath $LogFilePath -InputObject "######################################" -Append -Force
# Invoke-Expression $CurrentScriptFolder

# git pull request
######################################

Add-Content -Path $ActionStatusFile -Value "git pull command" -Force
Add-Content -Path $ActionStatusFile -Value $Splitter -Force
Add-Content -Path $ActionStatusFile -Value "Running command" -Force
$FullRunningCommand = "Start-Process -FilePath $RunCommand -Args $ArgsForRunningPullCommand  -RedirectStandardOutput $OutputStreamFile -RedirectStandardError $ErrorStreamFile"
Add-Content -Path $ActionStatusFile -Value $FullRunningCommand -Force

#Invoke-Expression $FullRunningCommand
Start-Process -FilePath $RunCommand -Args $ArgsForRunningPullCommand  -RedirectStandardOutput $OutputStreamFile -RedirectStandardError $ErrorStreamFile -Wait
if ($Error) {

    Add-Content -Path $ActionStatusFile -Value $PSErrorPresentString -Force
    Add-Content -Path $ActionStatusFile -Value $ErrorSplitter -Force
    Add-Content -Path $ActionStatusFile -Value ($Error[0].ToString() + $Error[0].InvocationInfo.PositionMessage) -Force
    Add-Content -Path $ActionStatusFile -Value $ErrorSplitter -Force
    Add-Content -Path $ActionStatusFile -Value "" -Force
    Add-Content -Path $ActionStatusFile -Value "" -Force
    $Error.Clear()
}

$TempOutPutContent = (Get-Content -Path $OutputStreamFile | Out-String)
if ($Error) {

    Add-Content -Path $ActionStatusFile -Value $PSErrorPresentString -Force
    Add-Content -Path $ActionStatusFile -Value $ErrorSplitter -Force
    Add-Content -Path $ActionStatusFile -Value ($Error[0].ToString() + $Error[0].InvocationInfo.PositionMessage) -Force
    Add-Content -Path $ActionStatusFile -Value $ErrorSplitter -Force
    Add-Content -Path $ActionStatusFile -Value "" -Force
    Add-Content -Path $ActionStatusFile -Value "" -Force
    $Error.Clear()
}

Add-Content -Path $ActionStatusFile -Value "Output content" -Force
Add-Content -Path $ActionStatusFile -Value $TempOutPutContent -Force

$TempErrorContent = (Get-Content -Path $ErrorStreamFile | Out-String)
if ($Error) {

    Add-Content -Path $ActionStatusFile -Value $PSErrorPresentString -Force
    Add-Content -Path $ActionStatusFile -Value $ErrorSplitter -Force
    Add-Content -Path $ActionStatusFile -Value ($Error[0].ToString() + $Error[0].InvocationInfo.PositionMessage) -Force
    Add-Content -Path $ActionStatusFile -Value $ErrorSplitter -Force
    Add-Content -Path $ActionStatusFile -Value "" -Force
    Add-Content -Path $ActionStatusFile -Value "" -Force
    $Error.Clear()
}

Add-Content -Path $ActionStatusFile -Value "Error content" -Force
Add-Content -Path $ActionStatusFile -Value $TempErrorContent -Force
Add-Content -Path $ActionStatusFile -Value $Splitter -Force
Add-Content -Path $ActionStatusFile -Value "" -Force
Add-Content -Path $ActionStatusFile -Value "" -Force

######################################

#Invoke-Expression "git pull"
# Start-Process -FilePath "git.exe" -Args "remote show origin"  -RedirectStandardOutput $OutputStreamFile -RedirectStandardError $ErrorStreamFile

# Start-Process -FilePath "git.exe" -Args "pull -v"  -RedirectStandardOutput $OutputStreamFile -RedirectStandardError $ErrorStreamFile
# -RedirectStandardInput "c:/Testsort.txt"

######################################

# Get git repo last commit
######################################

Add-Content -Path $ActionStatusFile -Value "Getting git last commit" -Force
Add-Content -Path $ActionStatusFile -Value $Splitter -Force
Add-Content -Path $ActionStatusFile -Value "Running command" -Force
$FullRunningCommand = "Start-Process -FilePath $RunCommand -Args $ArgsForGettingLastRepoCommit  -RedirectStandardOutput $OutputStreamFile -RedirectStandardError $ErrorStreamFile"
Add-Content -Path $ActionStatusFile -Value $FullRunningCommand -Force

#Invoke-Expression $FullRunningCommand
Start-Process -FilePath $RunCommand -Args $ArgsForGettingLastRepoCommit  -RedirectStandardOutput $OutputStreamFile -RedirectStandardError $ErrorStreamFile -Wait
if ($Error) {

    Add-Content -Path $ActionStatusFile -Value $PSErrorPresentString -Force
    Add-Content -Path $ActionStatusFile -Value $ErrorSplitter -Force
    Add-Content -Path $ActionStatusFile -Value ($Error[0].ToString() + $Error[0].InvocationInfo.PositionMessage) -Force
    Add-Content -Path $ActionStatusFile -Value $ErrorSplitter -Force
    Add-Content -Path $ActionStatusFile -Value "" -Force
    Add-Content -Path $ActionStatusFile -Value "" -Force
    $Error.Clear()
}

$TempOutPutContent = (Get-Content -Path $OutputStreamFile | Out-String)
if ($Error) {

    Add-Content -Path $ActionStatusFile -Value $PSErrorPresentString -Force
    Add-Content -Path $ActionStatusFile -Value $ErrorSplitter -Force
    Add-Content -Path $ActionStatusFile -Value ($Error[0].ToString() + $Error[0].InvocationInfo.PositionMessage) -Force
    Add-Content -Path $ActionStatusFile -Value $ErrorSplitter -Force
    Add-Content -Path $ActionStatusFile -Value "" -Force
    Add-Content -Path $ActionStatusFile -Value "" -Force
    $Error.Clear()
}

Add-Content -Path $ActionStatusFile -Value "Output content" -Force
Add-Content -Path $ActionStatusFile -Value $TempOutPutContent -Force

$TempErrorContent = (Get-Content -Path $ErrorStreamFile | Out-String)
if ($Error) {

    Add-Content -Path $ActionStatusFile -Value $PSErrorPresentString -Force
    Add-Content -Path $ActionStatusFile -Value $ErrorSplitter -Force
    Add-Content -Path $ActionStatusFile -Value ($Error[0].ToString() + $Error[0].InvocationInfo.PositionMessage) -Force
    Add-Content -Path $ActionStatusFile -Value $ErrorSplitter -Force
    Add-Content -Path $ActionStatusFile -Value "" -Force
    Add-Content -Path $ActionStatusFile -Value "" -Force
    $Error.Clear()
}

Add-Content -Path $ActionStatusFile -Value "Error content" -Force
Add-Content -Path $ActionStatusFile -Value $TempErrorContent -Force
Add-Content -Path $ActionStatusFile -Value $Splitter -Force
Add-Content -Path $ActionStatusFile -Value "" -Force
Add-Content -Path $ActionStatusFile -Value "" -Force

######################################


# Return to script folder
######################################

Add-Content -Path $ActionStatusFile -Value "Return to PS script folder" -Force
Add-Content -Path $ActionStatusFile -Value $Splitter -Force
Add-Content -Path $ActionStatusFile -Value $CurrentScriptFolder -Force

Set-Location $CurrentScriptFolder
if ($Error) {

    Add-Content -Path $ActionStatusFile -Value $PSErrorPresentString -Force
    Add-Content -Path $ActionStatusFile -Value $ErrorSplitter -Force
    Add-Content -Path $ActionStatusFile -Value ($Error[0].ToString() + $Error[0].InvocationInfo.PositionMessage) -Force
    Add-Content -Path $ActionStatusFile -Value $ErrorSplitter -Force
    Add-Content -Path $ActionStatusFile -Value "" -Force
    Add-Content -Path $ActionStatusFile -Value "" -Force
    $Error.Clear()
}
$TempCurrentFolder = (Get-Location).Path
if ($Error) {

    Add-Content -Path $ActionStatusFile -Value $PSErrorPresentString -Force
    Add-Content -Path $ActionStatusFile -Value $ErrorSplitter -Force
    Add-Content -Path $ActionStatusFile -Value ($Error[0].ToString() + $Error[0].InvocationInfo.PositionMessage) -Force
    Add-Content -Path $ActionStatusFile -Value $ErrorSplitter -Force
    Add-Content -Path $ActionStatusFile -Value "" -Force
    Add-Content -Path $ActionStatusFile -Value "" -Force
    $Error.Clear()
}

$TempString = (Get-ChildItem -Path $TempCurrentFolder | Out-String)
if ($Error) {

    Add-Content -Path $ActionStatusFile -Value $PSErrorPresentString -Force
    Add-Content -Path $ActionStatusFile -Value $ErrorSplitter -Force
    Add-Content -Path $ActionStatusFile -Value ($Error[0].ToString() + $Error[0].InvocationInfo.PositionMessage) -Force
    Add-Content -Path $ActionStatusFile -Value $ErrorSplitter -Force
    Add-Content -Path $ActionStatusFile -Value "" -Force
    Add-Content -Path $ActionStatusFile -Value "" -Force
    $Error.Clear()
}

Add-Content -Path $ActionStatusFile -Value $TempString -Force
Add-Content -Path $ActionStatusFile -Value $Splitter -Force
Add-Content -Path $ActionStatusFile -Value "" -Force
Add-Content -Path $ActionStatusFile -Value "" -Force

######################################
# Return to script folder
######################################

# $GoToScriptFolder = "cd " + $CurrentScriptFolder
# Invoke-Expression $GoToScriptFolder
# Set-Location $CurrentScriptFolder

# Out-File -FilePath $LogFilePath -InputObject $CurrentScriptFolder -Append -Force

######################################


# Restart Service
######################################

# Invoke-Expression $StartServiceCommand
Add-Content -Path $ActionStatusFile -Value "Restart Service" -Force
Add-Content -Path $ActionStatusFile -Value $Splitter -Force

Restart-Service -Name $ServiceName -Force
if ($Error) {

    Add-Content -Path $ActionStatusFile -Value $PSErrorPresentString -Force
    Add-Content -Path $ActionStatusFile -Value $ErrorSplitter -Force
    Add-Content -Path $ActionStatusFile -Value ($Error[0].ToString() + $Error[0].InvocationInfo.PositionMessage) -Force
    Add-Content -Path $ActionStatusFile -Value $ErrorSplitter -Force
    Add-Content -Path $ActionStatusFile -Value "" -Force
    Add-Content -Path $ActionStatusFile -Value "" -Force
    $Error.Clear()
}
Start-Sleep -Seconds 15
$TempServiceStatus = (Get-Service -Name $ServiceName).Status
if ($Error) {

    Add-Content -Path $ActionStatusFile -Value $PSErrorPresentString -Force
    Add-Content -Path $ActionStatusFile -Value $ErrorSplitter -Force
    Add-Content -Path $ActionStatusFile -Value ($Error[0].ToString() + $Error[0].InvocationInfo.PositionMessage) -Force
    Add-Content -Path $ActionStatusFile -Value $ErrorSplitter -Force
    Add-Content -Path $ActionStatusFile -Value "" -Force
    Add-Content -Path $ActionStatusFile -Value "" -Force
    $Error.Clear()
}

Add-Content -Path $ActionStatusFile -Value "Service status" -Force

Add-Content -Path $ActionStatusFile -Value $TempServiceStatus -Force
Add-Content -Path $ActionStatusFile -Value $Splitter -Force
Add-Content -Path $ActionStatusFile -Value "" -Force
Add-Content -Path $ActionStatusFile -Value "" -Force

# Out-File -FilePath $LogFilePath -InputObject "Restart Service $ServiceName" -Append -Force

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