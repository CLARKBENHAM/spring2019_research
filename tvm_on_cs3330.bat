@ECHO ON
ssh %CS3330% -t "mkdir research; module load python3; cd research; git clone --recursive https://github.com/dmlc/tvm; "
