
#include <iostream>
#include <vector>
#include <math.h>
// For Time
#include <time.h> 
#define BILLION  1000000000.0

//
using namespace std;


class Pair
{
    public:
    float x;
    float y;

    Pair(float a = 0, float b = 0)
    {
        x = a;
        y = b;
    }

    void dis()
    {
        cout << "(" << x << "," << y << ")   ";
    }
};

void display(vector<float> v)
{
    for (auto i = v.begin(); i != v.end(); i++)
    {
        cout << *i << "  ";
    }
    cout << endl;
}

extern "C"
vector<float> seq1(float start, int length, float step)
{
    vector<float> y;
    vector<float> x;

    int iterations = length*10;
    int i = 0;
    float count = start;
    int loopCount = 0;
    while(i < iterations)
    {
        y.push_back((round(count*1000.0) / 1000.0));
        if (i > 0)
            x.push_back((round(-count*1000.0) / 1000.0));
        if (i != iterations)
            count += step;
        i += 1;
        if (count > ((static_cast<float>(length)/2.0) + step))
            break;
    }

    vector<float> w;
    while (!x.empty())
    {
        w.push_back(x.back());
        x.pop_back();
    }

    for (auto i = y.begin(); i != y.end(); i++)
    {
        w.push_back(*i);
    }

    int x_num = w.size();
    // cout << "Total no. of X-coordinates: " << x_num << endl;
    return w;

}

extern "C"
vector<float> seq2(float start, int width, float step)
{
    vector<float> y;
    vector<float> x;

    int iterations = width*10;
    int i = 0;
    float count = start;
    while(i < iterations)
    {
        y.push_back((round(count*1000.0) / 1000.0));
        if (i > 0)
            x.push_back((round(-count*1000.0) / 1000.0));
        if (i != iterations)
            count += step;
        i += 1;

        if (count > (width/2.0))
            break;
    }

    vector<float> w;
    // Reversing the y array and adding it to
    // w
    while (!y.empty())
    {
        w.push_back(y.back());
        y.pop_back();
    }

    // extending w array with x array
    for (auto i = x.begin(); i != x.end(); i++)
    {
        w.push_back(*i);
    }

    int y_num = w.size();
    // cout << "Total no. of Y-coordinates: " << y_num << endl;
    return w;

}

extern "C"
int inscribe(float radius, int length, int width)
{
    float height = round((radius*sqrt(3))*1000.0) / 1000.0; // upto 3 - decimal
    vector<float> a = seq1(0.0 , length, height);
    vector<float> b = seq2(0.0 , width, radius);

    // getting the odd and even indexing value of index seperating b into even indexing and odd indexing of b
    vector<float> odd_ind;
    auto i = b.begin();
    i++;
    for (i; i != b.end(); i += 2)
    {
        odd_ind.push_back(*i);
    }

    vector<float> even_ind;
    i = b.begin();
    for (i; i != b.end(); i += 2)
    {
        even_ind.push_back(*i);
        if ((i + 1) == b.end())
            break;
    }

    // getting the odd and even columns value of index seperating a into even columns and odd columns  of a
    vector<float> odd_col;
    vector<float> even_col;
    for (int i = 0; i < a.size(); i++)
    {
        if (i%2 == 0)
            even_col.push_back(a[i]);
        else
            odd_col.push_back(a[i]);
    }


    // for placing the even columns
    vector < vector<Pair> > df1;
    for (int i = 0; i < even_ind.size(); i++)
    {
        vector <Pair> temp;
        for (int j = 0; j < even_col.size(); j++)
        {
            Pair c(even_col[j], even_ind[i]);
            temp.push_back(c);
        }
        df1.push_back(temp);
    }

    // for placing the odd columns
    for (int i = 0; i < odd_ind.size(); i++)
    {
        vector <Pair> temp;
        for (int j = 0; j < odd_col.size(); j++)
        {
            Pair c(odd_col[j], odd_ind[i]);
            temp.push_back(c);
        }
        df1.push_back(temp);
    }

    // Displaying and getting total count //
    int final_num = 0;
    for (auto i = df1.begin(); i != df1.end(); i++)
    {
        for (auto j = (*i).begin(); j != (*i).end(); j++)
        {
            // (*j).dis();
            final_num++;
        }
        // cout << endl;
    }

    // cout << "No. of circles that can be inscribed in " << length << "X" << width << " canvas: " << final_num << endl;

    return final_num;
    ///////////////
}


// int main()
// {
//     struct timespec start, end;
//     clock_gettime(CLOCK_REALTIME, &start);

//     inscribe(1, 50, 50);

//     clock_gettime(CLOCK_REALTIME, &end);

//     double time_spent = (end.tv_sec - start.tv_sec) +
//                         (end.tv_nsec - start.tv_nsec) / BILLION;
//     cout << "\n\nTotal Time for Execution(sec):   " << time_spent << endl;

//     return 0;
// }