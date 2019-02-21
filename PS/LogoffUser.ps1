function Get-Quser{
    param(
        [string]$Username,
        [Parameter(
            ValueFromPipeline=$true,
            ValueFromPipelineByPropertyName=$true
        )]
        [Alias('Name','Computer','Server')]
        [string]$ComputerName = $env:COMPUTERNAME,
        [switch]$Logoff
    )
    begin {
        $tmplt = @{
            ComputerName  = $null
            UserName      = $null
            SessionName   = $null
            SessionId     = $null
            State         = $null
            IdleTime      = $null
            LogonTime     = $null
            Error         = $null
        }
    }

    process {
        $hash = $tmplt.Clone()  # clear (gets an unused hash)
        $hash.ComputerName = $ComputerName
        try {
            quser /server:$Computer 2>&1 |
                Select-Object -Skip 1 |
                ForEach-Object {
                    $hash.ComputerName = $Computer
                    $hash.UserName = (-join $_[1 .. 20]).Trim()
                    $hash.SessionName = (-join $_[23 .. 37]).Trim()
                    $hash.SessionId = [int](-join $_[38 .. 44])
                    $hash.State = (-join $_[46 .. 53]).Trim()
                    $hash.IdleTime = [datetime](-join $_[54 .. 63]).Trim() - [datetime]::Today
                    $hash.LogonTime = [datetime](-join $_[65 .. ($_.Length - 1)])
                }
            }
            catch {
                $hash.Error = $_
            }
            if($username){
                if($Username -eq $hash.Username){
                    if($Logoff){
                        Write-Warning "Logging off $($hash.Username) from $ComputerName"
                        #logoff $hash.SessionId /SERVER:$computer
                    }
                }
            }else{
                [pscustomobject]$hash
            }
            Remove-Variable hash
        }
}

			
function Get-Quser-v1() 
{
param (
	[CmdletBinding()]
	[Parameter(ValueFromPipeline = $true,
			   ValueFromPipelineByPropertyName = $true)]
	[string[]]
	$ComputerName = 'localhost'
)
begin {
	$ErrorActionPreference = 'Stop'
}

process {
	foreach ($Computer in $ComputerName) {
		try {
			quser /Server:$ComputerName | Select-Object -Skip 1 | ForEach-Object {
				$CurrentLine = $_.Trim() -Replace '\s+', ' ' -Split '\s'
				$UserName = $CurrentLine[0]
				$UserID = $CurrentLine[1]
				$UserActivity = $CurrentLine[2]

				# If session is disconnected, all processes will be closed and the user logged out
				if ($UserActivity -match 'Disc') {
					Get-Process | Select -Property ID, SessionID | Where-Object { $_.SessionID -eq $UserID } | ForEach-Object { Stop-Process -ID $_.ID -Force -ErrorAction SilentlyContinue }
					Write-Warning "Logging off user $UserName"
					Logoff $UserID
				}
			}
		}
		catch {
			Write-Warning "Error occured - $($_.Exception.Message)"
		}
	}
}
}

function Get-Quser-v2([String]$user)
{
    		    $query_user = quser | Select-Object -Skip 1
                
                foreach ($Computer in $query_user)   
                {
				    $CurrentLine = $Computer.Trim() -Replace '\s+', ' ' -Split '\s'
                    $CurrentLine = $CurrentLine -Replace '>'
				    $UserName = $CurrentLine[0]
				    $UserID = $CurrentLine[1]
				    $UserActivity = $CurrentLine[2]

				    # If session is disconnected, all processes will be closed and the user logged out
				    if ($UserActivity -match 'Disc') 
                    {
					    Get-Process | Select -Property ID, SessionID | Where-Object { $_.SessionID -eq $UserID } | ForEach-Object { Stop-Process -ID $_.ID -Force -ErrorAction SilentlyContinue }
					    Write-Warning "Logging off user $UserName"
					    Logoff $UserID
				    }
    }
}

function LogoffCurrentUser()
{
    logoff -UserName "Ogurchuk"
}

#Get-Quser -Username Ogurchuk -Logoff
Get-Quser-v2 #
#Get-ULogged -ComputerName $env:COMPUTERNAME
#LogoffCurrentUser