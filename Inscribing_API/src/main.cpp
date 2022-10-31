#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <iostream>
#include <vector>
#include <math.h>
#include <time.h>
using namespace std;
namespace py = pybind11;

struct Point
{
    float x, y;
};

vector<float> seq1(float start, int length, float step)
{
    vector<float> y;
    vector<float> x;

    int iterations = length * 10;
    int i = 0;
    float count = start;
    int loopCount = 0;
    while (i < iterations)
    {
        y.push_back((round(count * 1000.0) / 1000.0));
        if (i > 0)
            x.push_back((round(-count * 1000.0) / 1000.0));
        if (i != iterations)
            count += step;
        i += 1;
        if (count > ((static_cast<float>(length) / 2.0) + step))
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
    return w;
}

vector<float> seq2(float start, int width, float step)
{
    vector<float> y;
    vector<float> x;

    int iterations = width * 10;
    int i = 0;
    float count = start;
    while (i < iterations)
    {
        y.push_back((round(count * 1000.0) / 1000.0));
        if (i > 0)
            x.push_back((round(-count * 1000.0) / 1000.0));
        if (i != iterations)
            count += step;
        i += 1;

        if (count > (width / 2.0))
            break;
    }

    vector<float> w;
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
    return w;
}

std::vector<Point> inscribe(float radius, int length, int width)
{
    float height = round((radius * sqrt(3)) * 1000.0) / 1000.0; // upto 3 - decimal
    vector<float> a = seq1(0.0, length, height);
    vector<float> b = seq2(0.0, width, radius);

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
        if (i % 2 == 0)
            even_col.push_back(a[i]);
        else
            odd_col.push_back(a[i]);
    }

    // for placing the even columns
    std::vector<Point> df1;
    for (int i = 0; i < even_ind.size(); i++)
    {
        for (int j = 0; j < even_col.size(); j++)
        {
            df1.push_back({even_col[j], even_ind[i]});
        }
    }
    // for placing the odd columns
    for (int i = 0; i < odd_ind.size(); i++)
    {
        for (int j = 0; j < odd_col.size(); j++)
        {
            df1.push_back({odd_col[j], odd_ind[i]});
        }
    }
    return df1;
}

// NOTE: The name given here must match the one given in CMakeLists.txt
PYBIND11_MODULE(geocoordinates, m)
{
    // Declare the point class
    py::class_<Point>(m, "Point")
        .def(py::init<float, float>()) // Point takes 2 longs to construct
        .def_readonly("x", &Point::x)
        .def_readonly("y", &Point::y);

    // Declare the solve function
    m.def(
        "inscribe", // Name in python
        &inscribe,  // Address of function
        "Returns a vector of points containing the center of circles");
}