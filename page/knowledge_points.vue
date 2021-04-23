<template>
	<view>
		<u-cell-group >
			<u-cell-item v-for="(item,index) in knowledge_list_dict" :key="item.knowledge" v-bind:title="item.knowledge" v-on:click="click_list(index)"></u-cell-item>
		</u-cell-group>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				knowledge_list_dict : new Array(),
				url:"http://127.0.0.1:8000/wxapp/getpractice",
				knowledge_list : new Array(),
				practice_list : new Array()
				
			}
		},
		onLoad:function(){
			
		},
		onLoad: function (option) { //option为object类型，会序列化上个页面传递的参数
		if(typeof(option.knowledge_point) != undefined){
			var str = new Array()
		    console.log(option.knowledge_point); //打印出上个页面传递的参数。
			str = option.knowledge_point.split(',')
			for(var i =0;i<str.length;i++){
				//console.log(str[i])
				this.knowledge_list.push(str[i].toString())
				this.knowledge_list_dict.push({knowledge:str[i]})
				}
//			console.log(this.knowledge_list)
			}
		},
		methods: {
			click_list:function(index){
				console.log(this.knowledge_list[index])
				uni.navigateTo({
					url:'/pages/classification/practice?type='+'classification'+'&knowledge_point='+
					this.knowledge_list[index]
				})
				/*this.$u.get(this.url,{
					knowledge_point:this.knowledge_list[index]
				})
				.then(res =>{
					for(var i = 0;i<res.length;i++){
						console.log(res[i])
						this.practice_list.push(res[i])
					}
					for(var i = 0;i<res.length;i++){
						console.log(this.practice_list[i].content)
					}
					uni.navigateTo({
						url:'/pages/classification/practice?knowledge_point='+
						this.
					})
				})
				.catch(error =>{
					console.log(error)
				})*/
			}
			
		}
	}
</script>

<style>

</style>
