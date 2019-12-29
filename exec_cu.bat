@ECHO ON
SET filename=temp.cu
SET num=17
::need to use putty instead?
scp %filename% %CS3330%:~\research\%filename%
ssh %CS3330%
::below only runs when return the the calling loc
scp research\%filename% cb5ye@automata%num%.cs.virginia.edu:~\research\%filename%
::SSH key for authpath?
::nvcc -o a.out example.cu
ssh cb5ye@automata%num%.cs.virginia.edu -t "cd research; nvcc -o a.out %filename%; ./a.out"
::ssh %CS3330% -t "cd CS3330/hclrs; module load python3; ./hclrs %filename% y86/%test% -d"
