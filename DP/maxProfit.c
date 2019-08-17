#include <stdio.h>
int maxProfit1(int* prices, int pricesSize){
    if (pricesSize == 0){
        return 0;
    }

    int maxProfit = 0;
    int buyPrice = prices[0];
    int sellPrice;
    for (int i=1;i<pricesSize;i++){
        if (prices[i]-buyPrice>maxProfit){
            maxProfit = prices[i]-buyPrice;
        }

        if (prices[i]-buyPrice<0){
            buyPrice = prices[i];
        }
    }
    return maxProfit;
}

int maxProfit2(int* prices, int pricesSize){
    if (pricesSize == 0){
        return 0;
    }

    int localMaxProfit = 0;
    int globalMaxProfit = 0;
    int buyPrice = prices[0];
    int sellPrice;
    for (int i=1;i<pricesSize;i++){
        if (prices[i]-buyPrice>localMaxProfit){
            localMaxProfit  = prices[i]-buyPrice;
        }

        if (prices[i]-prices[i-1]<0){
            buyPrice = prices[i];
            globalMaxProfit += localMaxProfit;
            localMaxProfit = 0;
            printf("%d\n", globalMaxProfit);
        }
    }
    globalMaxProfit += localMaxProfit;
    return globalMaxProfit;
}


int maxProfit3(int* prices, int pricesSize){
    if (pricesSize == 0){
        return 0;
    }

    int profit1st = 0;
    int profit2nd = 0;
    int localProfit = 0;
    int buyPrice = prices[0];

    for (int i=1;i<pricesSize;i++){
            if (prices[i]-buyPrice>localProfit){
                localProfit = prices[i] - buyPrice;
                // printf("%s%d\n", "local:", localProfit);
            }

            if (prices[i]-prices[i-1]<0){
                buyPrice = prices[i];

                if (profit1st<localProfit){
                    profit2nd = profit1st;
                    profit1st = localProfit;
                }else if (profit2nd<localProfit){
                    profit2nd = localProfit;
                }else{
                    ;
                }
                localProfit = 0;
                printf("%d\n", profit1st+profit2nd);
            }
    }

    if (profit1st<localProfit){
        profit2nd = profit1st;
        profit1st = localProfit;
    }else if (profit2nd<localProfit){
        profit2nd = localProfit;
    }else{
        ;
    }
    
    return profit1st+profit2nd;
    
}

int main(){
    int prices[10] = {1,2,4,2,5,7,2,4,9,0}; 
    int pricesSize = 10;
    int maxProfitOut;

    maxProfitOut = maxProfit3(prices, pricesSize);
    printf("%d", maxProfitOut);
}