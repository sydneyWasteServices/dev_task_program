# How to test only grep one file 
# Since I am going to rm one file only
ICSV=$(cat '../list.csv' | cut -d, -f1)
for id in $ICSV
do 
    ls ./ | if [ "$(grep -c -w $id)" -gt 1 ]; then 
        # more than one match
        echo $id;
        echo $(ls ./ | grep $id -w); else
        ls ./ | grep -w $id | xargs -d '\n' rm
    fi
done
# let "COUNT+=1"
# echo $COUNT
# COUNT=$[$COUNT +1]
# let COUNT++
# echo $COUNT
# equal to 1 -> rm
# -0 -d "\n" -exec rm
# $(ls ./ | grep $id -w)
# echo $( ls ./ | grep $id -c -w);
# $(ls ./ | grep $id -c)
# issues - the ternary even larger than 1 is True 
# l | grep 1115 -w -c | echo $(( xargs > 1 ))
# /c/Users/Gordon.Tang/Desktop/codes/repo/dev_task_program/task_program/JLL/mv_files_grep_last_field/main.sh




# Microsoft.Data.SqlClient.SqlException (0x80131904): A network-related or instance-specific error occurred 
# while establishing a connection to SQL Server. The server was not found or was not accessible.
 
# Verify that the instance name is correct and that SQL Server is configured to allow remote connections. 
# (provider: TCP Provider,
#  error: 0 - A connection attempt failed because the connected party did not properly respond after a period of time, 
#  or established connection failed because connected host has failed to respond.)
#  ---> System.ComponentModel.Win32Exception (10060): A connection attempt failed 
#  because the connected party did not properly respond after a period of time, 
#  or established connection failed because connected host has failed to respond.
#    at Microsoft.Data.SqlClient.SqlInternalConnection.OnError(SqlException exception, Boolean breakConnection, Action`1 wrapCloseInAction)
#    at Microsoft.Data.SqlClient.TdsParser.ThrowExceptionAndWarning(TdsParserStateObject stateObj, Boolean callerHasConnectionLock, Boolean asyncClose)
#    at Microsoft.Data.SqlClient.TdsParser.Connect(ServerInfo serverInfo, SqlInternalConnectionTds connHandler, Boolean ignoreSniOpenTimeout, Int64 timerExpire, Boolean encrypt, Boolean trustServerCert, Boolean integratedSecurity, Boolean withFailover, SqlAuthenticationMethod authType)
#    at Microsoft.Data.SqlClient.SqlInternalConnectionTds.AttemptOneLogin(ServerInfo serverInfo, String newPassword, SecureString newSecurePassword, Boolean ignoreSniOpenTimeout, TimeoutTimer timeout, Boolean withFailover)
#    at Microsoft.Data.SqlClient.SqlInternalConnectionTds.LoginNoFailover(ServerInfo serverInfo, String newPassword, SecureString newSecurePassword, Boolean redirectedUserInstance, SqlConnectionString connectionOptions, SqlCredential credential, TimeoutTimer timeout)
#    at Microsoft.Data.SqlClient.SqlInternalConnectionTds.OpenLoginEnlist(TimeoutTimer timeout, SqlConnectionString connectionOptions, SqlCredential credential, String newPassword, SecureString newSecurePassword, Boolean redirectedUserInstance)
#    at Microsoft.Data.SqlClient.SqlInternalConnectionTds..ctor(DbConnectionPoolIdentity identity, SqlConnectionString connectionOptions, SqlCredential credential, Object providerInfo, String newPassword, SecureString newSecurePassword, Boolean redirectedUserInstance, SqlConnectionString userConnectionOptions, SessionData reconnectSessionData, Boolean applyTransientFaultHandling, String accessToken, DbConnectionPool pool)
#    at Microsoft.Data.SqlClient.SqlConnectionFactory.CreateConnection(DbConnectionOptions options, DbConnectionPoolKey poolKey, Object poolGroupProviderInfo, DbConnectionPool pool, DbConnection owningConnection, DbConnectionOptions userOptions)
#    at Microsoft.Data.ProviderBase.DbConnectionFactory.CreateNonPooledConnection(DbConnection owningConnection, DbConnectionPoolGroup poolGroup, DbConnectionOptions userOptions)
#    at Microsoft.Data.ProviderBase.DbConnectionFactory.<>c__DisplayClass48_0.<CreateReplaceConnectionContinuation>b__0(Task`1 _)
#    at System.Threading.Tasks.ContinuationResultTaskFromResultTask`2.InnerInvoke()
#    at System.Threading.ExecutionContext.RunInternal(ExecutionContext executionContext, ContextCallback callback, Object state)
# --- End of stack trace from previous location ---
#    at System.Threading.Tasks.Task.ExecuteWithThreadLocal(Task& currentTaskSlot, Thread threadPoolThread)
# --- End of stack trace from previous location ---
#    at Microsoft.SqlTools.ServiceLayer.Connection.ReliableConnection.ReliableSqlConnection.<>c__DisplayClass30_0.<<OpenAsync>b__0>d.MoveNext() in D:\a\1\s\src\Microsoft.SqlTools.ManagedBatchParser\ReliableConnection\ReliableSqlConnection.cs:line 312
# --- End of stack trace from previous location ---
#    at Microsoft.SqlTools.ServiceLayer.Connection.ConnectionService.TryOpenConnection(ConnectionInfo connectionInfo, ConnectParams connectionParams) in D:\a\1\s\src\Microsoft.SqlTools.ServiceLayer\Connection\ConnectionService.cs:line 559
# ClientConnectionId:00000000-0000-0000-0000-000000000000
# Error Number:10060,State:0,Class:20