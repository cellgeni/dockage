FROM julia:1.10

ENV LazyModules_lazyload=false

RUN apt-get update && apt-get install -y build-essential

ENV JULIA_NUM_THREADS=30
ENV JULIA_CPU_TARGET="cascadelake,skylake-avx512,znver3;clone_all"
ENV BAYSOR_VERSION=v0.7.1
RUN julia -e 'using Pkg; Pkg.add(PackageSpec(url="https://github.com/kharchenkolab/Baysor.git", rev=ENV["BAYSOR_VERSION"])); Pkg.build()'

#RUN echo "export PATH=/root/.julia/bin/:$PATH" >> ~/.bashrc
#RUN echo "alias julia='/usr/local/julia/bin/julia --sysimage=/root/.julia/scratchspaces/cc9f9468-1fbe-11e9-0acf-e9460511877c/sysimg/libbaysor.so'" >> ~/.bashrc
#RUN ln -s /root/.julia/bin/baysor /usr/local/bin/baysor

#RUN /root/.julia/bin/baysor --help

#ENTRYPOINT ["/bin/bash"]
#WORKDIR /root/
