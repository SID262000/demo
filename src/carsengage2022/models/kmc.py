class Kmean():
    def __init__(self,data,limit)   #limit is the cluster limit that we want
        self.data=data
        self.limit=limit
    
    def optimal_cluster_elbow_method(self,ready_data):
        self.score=[]
        self.range_values=range(1,self.limit)
        self.scaler=StandardScaler()
        self.data_scaled=self.scaler.fit_transform(ready_data)

        for i in self.range_values:
            self.kmeans=KMeans(n_clusters=i)
            self.kmeans.fit(self.data_scaled)
            self.scores.append(self.kmeans.inertia_) #kmeans.inertia gives WCSS
    
        plt.plot(self.scores,'bx--')
        plt.title('Right number of clusters')
        plt.xlabel('clusters')
        plt.ylabel('WCSS')
        plt.show()  

    def k_means(self,cluster_number,ready_data):
        self.kmean=KMeans(cluster_number).fit(ready_data)
        self.labels=self.kmean.labels_
        self.clusters_centres=self.scaler.inverse_transform(self.kmean.cluster_centres_)
        self.clusters_centroids=pd.DataFrame(data=self.clusters_centres,columns=[self.data.columns])
        self.clusters_centroids.to_csv('Centroid_details.csv')
        self.max_label=self.labels.max()
        self.min_label=self.labels.min()
        print(f'Range of clusters is from {self.min_label} to {self.max_label}')
        self.y_kmeans=self.kmean.fit_predict(self.data_scaled)
        self.data_with_clusters=pd.concat([self.data,pd.DataFrame({'cluster':self:labels})].axis=1)
        self.data_with_clusters.to_csv('Clustered_data.csv')
        return self.data_with_clusters