
function Logoff-AllUsers()
{
  
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

        $hash = $tmplt.Clone()
    		    
                $query_user = quser | Select-Object -Skip 1
                
                
                foreach ($CurrentLine in $query_user)   
                {
                    $hash.ComputerName = $env:COMPUTERNAME
                    $hash.UserName = (-join $CurrentLine[1 .. 20]).Trim() -Replace '>'
                    $hash.SessionName = (-join $CurrentLine[23 .. 37]).Trim()
                    $hash.SessionId = [int](-join $CurrentLine[38 .. 44])
                    $hash.State = (-join $CurrentLine[46 .. 53]).Trim()
                    $hash.IdleTime = (-join $CurrentLine[54 .. 63]).Trim()
                    $hash.LogonTime = (-join $CurrentLine[65 .. ($CurrentLine.Length - 1)])
       			    Logoff $hash.SessionId
				    
				}
}


Logoff-AllUsers
