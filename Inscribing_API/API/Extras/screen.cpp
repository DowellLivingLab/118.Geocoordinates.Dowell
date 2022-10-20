#include <X11/Xlib.h>
#include <iostream>
using namespace std;

int main()
{
    Display *d = XOpenDisplay(0);
    // Screen* s = d->screen();
    cout << DefaultScreenOfDisplay(d);
    // int a = s->height;
    // int b = s->width;
    // cout << a << endl
    //      << b << endl;
}