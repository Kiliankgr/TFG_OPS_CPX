#include <cstdio>
#include <iostream>
#include <fstream>
#include <string>
#include <cstring>

#include <cstdlib>

#include "OPS_instance_t.hpp"
#include "OPS_input_t.hpp"
#include "OPS_output_t.hpp"

#include "solvers.hpp"

using ordered_json = nlohmann::json;
using namespace std;
using namespace EMIR;
/*
void write_results_works(std::vector<int> works, std::string out_file_name);
void write_results_times(vector<double> times, string out_file_name);
*/
void write_results(OPS_output_t out_ops, string file_name);
void obtain_only_selected_elements(vector<int> &obj_seleccionados, vector<double> &momentos_seleccionados);

void read(const string &file_name, OPS_instance_t &instance)
{
    ifstream input_file(file_name);

    instance.read(input_file);
    input_file.close();
}

//Ficheros usados para el procesamiento
int processor(const string &ins_file,
              const string &sta_file,
              const string &log_file,
              const string &results_file,
              const int id)
{
    //Leemos y obtenemos los datos del fichero instancia
    OPS_instance_t I; 
    read(ins_file, I);
    //Con la informacion obtenida de la instancia
    OPS_input_t In(I);
    const double tol = 1E-4;

    OPS_output_t Out(In);
    //NOTA:: Seguramente si queremos añadir la información de los resultados deberemos de trabajar con OPS_OUT
    ofstream O_file(sta_file, std::ios_base::app);
    ofstream L_file(log_file);

    (*solver_array[id])(&In, tol, Out, L_file, O_file);
    //Quitar, resulta que solo erab información "boba", nombre del fichero instancia, coste optimo estimado,precisión, si se encontró, si era optimo
    /*cout  << "\n Veamos que se escribe aqui---------------------------\n";
    Out.write_statistics(std::cout);
    cout  << "\n Veamos que se escribe aqui---------------------------\n";
    In.write_statistics(std::cout);
    cout  << "\n Veamos que se escribe aqui---------------------------\n";
    In.write_statistics_hdr(std::cout);
    */
    O_file << endl;
    O_file.close();

    L_file << endl;
    L_file.close();
    //Resultados 
    if ( results_file != "NONE") {
        write_results(Out, results_file);
    }
    /*cout << "Main.cpp: Valores de Y(trabajos seleccionados):\n";
    if ( works_file != "NONE") {
        write_results_works(Out.y_, works_file);
    }
    cout << "Main.cpp: Valores de S(trabajos tiempo):\n";
    if ( times_file != "NONE") {
        cout << "Escribir resultados";
        write_results_times(Out.s_, times_file);
    }*/
    
    return 0;
}
/*
void write_results(OPS_output_t out_ops, string file_name) {
    double total = 0;
    for(auto elem: out_ops.s_) {
        total += elem;
    }
    //cout << "\nTotal: " << total << endl;
    ordered_json j;
    j["valor_beneficio"] = out_ops.get_obj(); //Cambiar nombre
    // Al parecer hay un problema con como se guarda, debemos mover los elementos un slot para que concuerden 1 =>2 ultimo =>primero
    vector <int> obj_seleccionados;
    if (out_ops.y_.empty()) return;
    obj_seleccionados.resize(out_ops.y_.size());
    int ultimo = out_ops.y_.back();  // Guardamos el último
    for (int i = out_ops.y_.size() - 1; i > 0; --i) {
        obj_seleccionados[i] = out_ops.y_[i - 1];  // Cada elemento toma el valor del anterior
    }
    obj_seleccionados[0] = ultimo;
    vector <double> momentos_seleccionados = out_ops.s_;
    //vamos a guardar solo los elementos sellcionados por ende eliminamos los que no, y guardamos los que sí por su valor numérico
    //obtain_only_selected_elements(obj_seleccionados, momentos_seleccionados);
    j["objetos_seleccionados"] = obj_seleccionados;
    j["momento_seleccionado"] = momentos_seleccionados;

    ofstream out_file(file_name);  
    out_file << j.dump(4); 
    out_file.close();
}
*/
void write_results(OPS_output_t out_ops, string file_name) {
    ordered_json j;
    j["valor_beneficio"] = out_ops.get_obj(); 
    
    vector <int> obj_seleccionados = out_ops.y_;
    
    // Al parecer hay un problema con como se guarda, debemos mover los elementos un slot para que concuerden 2 =>1 PRIMERO => ULTIMO
    vector <double> momentos_seleccionados;
    if (out_ops.s_.empty()) return;
    
    double valor_primero = out_ops.s_.back();  // Guardamos el  primero
  

    for (int i = 0; i < out_ops.s_.size() - 1; i++) {
        momentos_seleccionados.push_back(out_ops.s_[i + 1]);  // Cada elemento toma el valor del siguiente
    }

    momentos_seleccionados.push_back(valor_primero);

    
    //vamos a guardar solo los elementos sellcionados por ende eliminamos los que no, y guardamos los que sí por su valor numérico

    obtain_only_selected_elements(obj_seleccionados, momentos_seleccionados);
    

    j["objetos_seleccionados"] = obj_seleccionados;
    j["momento_seleccionado"] = momentos_seleccionados;

    ofstream out_file(file_name);  
    out_file << j.dump(4); 
    out_file.close();
}

void obtain_only_selected_elements(vector<int> &_obj_seleccionados, vector<double> &_momentos_seleccionados) {
    vector <int> new_obj_seleccionados;
    vector <double> new_momentos_seleccionados;  

    
    //Ignoraremos el primer y ultimo elemento ya que fueron elementos "falsos"
    for (int i = 1; i < _obj_seleccionados.size() - 1; i++) {
        if(_obj_seleccionados[i] == 1) {
            new_obj_seleccionados.push_back(i); //pasamos la posicion, como el número del obj tenemos en cuenta que como el primer elemento y ultimo no existen realmente elemento_en_cuestion = pos_en_vector
            new_momentos_seleccionados.push_back(_momentos_seleccionados[i]);
        }
    }
    
    _obj_seleccionados = new_obj_seleccionados;
    _momentos_seleccionados = new_momentos_seleccionados;

    //cout << "\nTamaño del vector" << _obj_seleccionados.size() << ", " << _momentos_seleccionados.size();
}


int main(int argc, char **argv)
{
    int exit_code = 0;
    cout << "-----------------Modelo OPS_CPX------------------\n";
    
    if (argc > 1 && strcmp(argv[1], "-h") == 0) {
        cout << "Para la correcta ejecución del programa debera de ser tal que \"emir_cpx <temp_file> <instace_file> <output_log_file> <\" donde:\n"<<
                    " \"temp_file\": Fichero temporal el cual se usará para ciertos cálculos\n" <<
                    " \"instace_file\": Fichero con la instancia del problema\n" <<
                    " \"output_log_file\": Fichero de salida con el resultado\n"
                    " \"resultados_seleccionados_file\": Fichero de salida con los objetos seleccionados,tiempo ...\n";
        return exit_code;
    }
    
    if (argc == 4) {
        /*
         *  argv[1]       Target file       - Fichero temporal
         *  argv[2]       Instance file     - Instacia con los parametros de los objetos y varillas(distancias entre ellos, ubicación, tiempo...)
         *  argv[3]       Output log file   - Fichero con información acerca del tiempo de ejecución soluciones ...
         */
        const string sta_file(argv[1]);
        const string ins_file(argv[2]);
        const string log_file(argv[3]);
        const string results_file("NONE");
        
        const int id = 0;
        
        exit_code = processor(ins_file,
                              sta_file,
                              log_file,
                              results_file,
                              id);
        
        return exit_code;
    }

    if (argc == 5) {
        /*
         *  argv[1]       Target file       - Fichero temporal
         *  argv[2]       Instance file     - Instacia con los parametros de los objetos y varillas(distancias entre ellos, ubicación, tiempo...)
         *  argv[3]       Output log file   - Fichero con información acerca del tiempo de ejecución soluciones ...
         */
        const string sta_file(argv[1]);
        const string ins_file(argv[2]);
        const string log_file(argv[3]);
        const string results_file(argv[4]);
        cout << "\n5 Argumentos \n";
        const int id = 0;
        
        exit_code = processor(ins_file,
                              sta_file,
                              log_file,
                              results_file,
                              id);
        
        return exit_code;
    }
    /**
    if (argc == 7) {//No realizado aún

        /*
         *  argv[1]       Target file
         *  argv[2]       Instance file
         *  argv[3]       Output log file
         *  argv[4]       Output sol file
         *  argv[5]       Output sta file
         *  argv[6]       Solver ID
         

        const string sta_file(argv[1]);
        const string ins_file(argv[2]);
        const string log_file(argv[3]);
        
        const int id = atoi(argv[4]) - 1;

        const string sta_file("tmp.txt");
        const string ins_file("/home/kilian/Escritorio/TFG/Proyecto/OPS_CPX/test_ins.txt");
        const string log_file("test_log.txt");

        const int id = 0;

        exit_code = processor(ins_file,
                              sta_file,
                              log_file,
                              id);
        return exit_code;
    }
    */
    return exit_code;
}
