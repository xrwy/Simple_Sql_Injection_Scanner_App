from flask import Flask, render_template, request
import requests


app = Flask(__name__)

meta = ['&', ';', '`', "'", '\\', '"', '|', '*', '?', '~', '<', '>', '^', '(', ')', '[', ']', '{', '}', '$']

@app.route('/', methods = ['GET'])
def main():
    return render_template('sql_injection.html')

@app.route('/sql_injection_result', methods = ['GET','POST'])
def sqlInjectionResult():
    error_in_MYSQL_Databases = []
    error_in_MSSQL_Databases = []
    error_in_POSTGRES_Databases = []
    error_in_ORACLE_Databases = []
    sqlInjectionQuerys = []
    
    if request.method == 'POST':
        target_domain = request.form['target_domain']
        for meta_ in meta:
            new = target_domain + meta_
            sqlInjectionQuerys.append(new)
            res = requests.get(new)
            if 'mysql' in res.text.lower():         
                error_in_MYSQL_Databases.append('{} --> MYSQL Error.'.format(res))
                break
            elif 'native client' in res.text.lower(): 
                error_in_MSSQL_Databases.append('{} --> MSSQL Error.'.format(res))
                break
            elif 'syntax error' in res.text.lower(): 
                error_in_POSTGRES_Databases.append('{} --> POSTGRESQL Error.'.format(res))
                break
            elif 'ORA' in res.text.lower():    
                error_in_ORACLE_Databases.append('{} --> ORACLE Error.'.format(res))
                break
            else:
                pass

        if len(error_in_MYSQL_Databases) == 0:
            error_in_MYSQL_Databases = 0
        else:
            pass
        if len(error_in_MSSQL_Databases) == 0:
            error_in_MSSQL_Databases = 0
        else:
            pass
        if len(error_in_POSTGRES_Databases) == 0:
            error_in_POSTGRES_Databases = 0
        else:
            pass
        if len(error_in_ORACLE_Databases) == 0:
            error_in_ORACLE_Databases = 0
        else:
            pass
        if len(sqlInjectionQuerys) == 0:
            sqlInjectionQuerys = 0
        else:
            pass
        
        return render_template('sql_injection_result.html', 
        sqlInjectionQuerys = sqlInjectionQuerys,
        error_in_MYSQL_databases = error_in_MYSQL_Databases,
        error_in_MSSQL_databases = error_in_MSSQL_Databases,
        error_in_POSTGRES_databases = error_in_POSTGRES_Databases,
        error_in_ORACLE_databases = error_in_ORACLE_Databases
        )

    else:
        return 'For post requests only.'
 
if __name__== '__main__':
    app.run(debug=True, port=5000)


