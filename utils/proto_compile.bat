set SRC_DIR=..\src\tool
set MESSAGES_DIR=%SRC_DIR%\messages

protoc.exe -I=%SRC_DIR% --python_out=%SRC_DIR% %MESSAGES_DIR%\messages.proto