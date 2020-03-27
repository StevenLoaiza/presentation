#create year column
def create_yr(data, colname):
    """
        Parameters
        ----------
        data : DataFrame
            The dataframe
        colname: date
            The column name you want converted into a year
    """

    data['year']=data[colname].dt.year
    return data

#rename a column in place
def rename_col(data,old,new):
    data.rename(columns={old:new},inplace=True)
    return data

# univariate filtering
def filtering(dataf,col,filter1,option):
   # print('\''+col+'\'')
    list = []
    list.append(col)
    if option=='equal':
        a=dataf[dataf[list[0]] == filter1].reset_index(drop=True)
    elif option=='greater':
        a=dataf[dataf[list[0]] > filter1].reset_index(drop=True)
    elif option=='less':
        a=dataf[dataf[list[0]] < filter1].reset_index(drop=True)
    elif option=='na':
        a=dataf.dropna(subset=[list[0]]).reset_index(drop=True)
    return a

#create func to create figure
def simple_plot(data,ycol,xcol,label1,title,xaxis,yaxis,ymin,ymax):
    #lib
    import matplotlib.pyplot as plt
    import numpy as np
    import matplotlib.dates as mdates

    #call fig
    #plt.style.use(style)
    fig = plt.figure() 
    plt.rcParams["figure.figsize"] = (15,8)
    plt.ticklabel_format(axis="x",style="plain")

    ax = plt.axes(xlim=(data[xcol][0], data[xcol].iloc[-1]), ylim=(ymin, ymax)) 

    line_u, = ax.plot(data[xcol],data[ycol], color='blue',linestyle='dashed',label=label1)

    #add legend
    plt.legend()
    #gridline
    plt.grid()
    # setting a title for the plot 
    plt.title(title,fontsize=18) 
    # Add x and y lables, and set their font size
    plt.xlabel(yaxis, fontsize=20)
    plt.ylabel(xaxis, fontsize=20)
    # Set the font size of the number lables on the axes
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)