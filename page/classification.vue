<template>
	<view>
		<u-gap height="10" bg-color="#ffffff"></u-gap>
		<u-cell-group>
				<u-cell-item icon="grid-fill" title="按年级分类题库" v-on:click="grade_points"></u-cell-item>
				<u-cell-item icon="list" title="按知识点分类题库" value=""  v-on:click="knowlodge_points"></u-cell-item>
				<u-cell-item icon="level" title="个性化题目推荐" value="" v-on:click="personalize"></u-cell-item>
			</u-cell-group>
		<view>
			<uniModel :textmsg="textmsg" @cancel=operation(1) @confirm=operation(2) v-show="showTextmsg"></uniModel>
		</view>
	</view>
</template>
<script>
	import uniModel from '@/components/m-window.vue'
	export default {
		data() {
			return {
				user:{
					formula:'4*5'
				},
				knowledges_list : new Array(),
				showTextmsg:false,
				textmsg:{
					title:'您还没登录',
				    content:'请先登录再进行操作',
				    contentTwo :'',
				    cancel:'取消',
				    confirm:'去登录'
				        }
			};
		},
		components: {
		        uniModel
		    },
		methods:{
			grade_points:function(){
				
			},
			knowlodge_points:function(){
				if(this.$store.state.userID === ''){
					this.showTextmsg = true
				}
				else{
				this.knowledges_list = new Array()
				console.log('正在调用方法')
				this.$u.get('http://127.0.0.1:8000/wxapp/knowledgepoints', {
					
				})
				.then(res => {
					for(var i = 0;i<res.length;i++){
						//console.log(res[i].knowledge_point)
						this.knowledges_list.push(res[i].knowledge_point)
						}
					//console.log(typeof(res))
					//console.log(this.knowledges_list)
					uni.navigateTo({
						url:'/pages/classification/knowledge_points?knowledge_point='+
						this.knowledges_list
						})
					})
					.catch(err => {
						console.log(err)
					})
				}
			},
			personalize:function(){
				if(this.$store.state.userID === ''){
					this.showTextmsg = true
				}
				else{
				uni.navigateTo({
					url:'/pages/classification/personnalization_practice'
				})
				}
			},
			operation(e) {
			    let that = this
			    let type  = e
			    console.log(type)
			    if(type == 1){
			        //取消操作
			        that.showTextmsg = false
			        }
				else{
			        //确定操作
			        uni.switchTab({
			        	url:'/pages/profile/profile'
			        })
			        that.showTextmsg = false
			        }
	}
},
}

</script>

<style>
	.box1{
		width: 200px;
		height: 100px;
		background: #63c3ff;
		}
	.box2{
		width: 200px;
		height: 100px;
		background: #ffff7f;
		}
	.box1-click{
		background: #4CD964;
	}
	.box2-click{
		background: #4CD964;
	}
</style>
