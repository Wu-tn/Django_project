<template>
	<view>
		<view>
			<u-image mode="widthFix" :src="url">
				<u-loading slot="loading"></u-loading>
			</u-image>
		</view>
		<!--<view v-if="content_if">{{pratice_content}}</view>-->
		<u-divider height=300>请选择选项</u-divider>
		<view>
			<u-row gutter="0" justify="around">
				<u-col span="6" v-for="(item,index) in option_list">
					<view>{{Option_ABCD[index]}}</view>
					<u-button shape="square" size="medium" v-on:click="answer_click(index)" v-bind:disabled="disable_answer">{{item}}</u-button>
				</u-col>
			</u-row>
		</view>
		<view>
			<u-toast ref="uToast" />
		</view>	
		<view v-if="show_correct_option" class="red" >正确选项为:{{correct_option}}</view>
		<u-gap height="80" bg-color="#ffffff"></u-gap>
		<view class="wrap">
			<u-row gutter="8" align="center">
				<u-col span="6">
					<u-button type="primary" size="medium" v-on:click="backClcik">返回主页</u-button>
				</u-col>
				<u-col span="6">
					<u-button type="primary" size="medium" v-on:click="nextClick">下一题</u-button>
				</u-col>
			</u-row>
		</view>
		<view>
			<u-notice-bar mode="horizontal" :list="list"></u-notice-bar>
		</view>
	</view>
</template>

<script>
	import {  
	        mapState,  
	        mapMutations  
	    } from 'vuex';  
	export default {

		onLoad:function() {
			this.list = []
			//console.log(this.$store.state.userID)
			this.$options.methods.get_personalized_practice.bind(this)()
				
				
			},
		data() {
			return {
				Option_ABCD : ['A','B','C','D'],
				getPracticeUrl:'http://127.0.0.1:8000/wxapp/personalization',
				getSinglePracticeUrl:'http://127.0.0.1:8000/wxapp/getSinglePractice',
				answerUrl:'http://127.0.0.1:8000/wxapp/answerPersonnalization',
				type:"",
				knowledge_point:"",
				pratice_content_type:"",
				practice_content:"",
				pratice_list:new Array(),
				content_if:false,
				pratice_content:"",
				pic_if:false,
				pic_url:"http://www.ppxstark.xyz:9000/",
				url:"",
				option_list:new Array(),
				temp_list:['A','B','C','D'],
				correct_option:"",
				show_correct_option:false,
				disable_answer:false,
				answer_correct_or_not:true,
				practice_id:"",
				length:0,
				list: []
				
				
			}
		},
		methods: {
			showCorrectToast:function() {
				this.$refs.uToast.show({
					title: '回答正确',
					type: 'success'
				})
				}
				,
			showWrongToast:function(){
				this.$refs.uToast.show({
					title:"回答错误",
					type:'error'
				})
			},
			get_personalized_practice:function(){
				this.$u.get(this.getPracticeUrl,{
					userID:this.$store.state.userID
				})
				.then(res =>{
					console.log(res)
					for(var i in res){
						this.length++
					}
					for(var i = 0;i<this.length;i++){
						console.log(res[i])
						this.pratice_list.push(res[i].toString())
					}
//					console.log(res[0])
					this.show_practice()
					
				})
				.catch(error =>{
					console.log(error)
				})
				
			},
			/*getSinglePractice:function(){
				this.$u.get(this.getSinglePracticeUrl,{
					
				})
			},*/
			show_practice:function(){
				var number = parseInt(Math.random()*(this.pratice_list.length-1), 10)
				//var number = Math.round(Math.random()*this.pratice_list.length-1)
				console.log(number)
				console.log(this.pratice_list)
				this.$u.get(this.getSinglePracticeUrl,{
					number:this.pratice_list[number]
				})
				.then(res=>{
					console.log(res)
					var content = res[0].content.toString()
					console.log(content)
					this.practice_id = content
					this.url = this.pic_url + content.toString()
					console.log(this.url)
					var option_A = res[0].option_A
					var option_B = res[0].option_B
					var option_C = res[0].option_C
					var option_D = res[0].option_D
					this.correct_option = res[0].correct_option
					this.option_list.push(option_A)
					this.option_list.push(option_B)
					this.option_list.push(option_C)
					this.option_list.push(option_D)
					console.log(this.option_list)
					//if(content.slice(content.length-3,content.length-1) == 'jpg'){
					//console.log("---loading picture---")
					this.pic_if = true
					//}
						
					/*else{
						this.content_if=true
						this.pratice_content = content
						console.log(this.practice_content)
					}*/
				})
				.catch(error =>{
					console.log(error)
				})
			},
			answer_click:function(index){
				if(this.temp_list[index] === this.correct_option){
					this.answer_correct_or_not = true
					this.showCorrectToast()
					}
				else{
					this.showWrongToast()
					this.answer_correct_or_not = false
					}
				this.disable_answer = true
				this.show_correct_option = true
				var PracticeID = this.practice_id.split(".")[0].toString()
				console.log(PracticeID)
				this.$u.get(this.answerUrl,{
					user_id:this.$store.state.userID,practice_id:PracticeID,answer:this.answer_correct_or_not
				})
				.then(res =>{
					console.log(res)
					this.list.push(res)
				})
				.catch(error =>{
					console.log(error)
				})
			
			},
			backClcik:function(){
				//pages = getCurrentPages()
				uni.navigateBack({
					delta:getCurrentPages().length-1,
					animationDuration:1000,
					animationType:'pop-out'
				})
			},
			nextClick:function(){
				uni.redirectTo({
					url:'/pages/classification/personnalization_practice'
				})
			}
			
		}
	}
</script>

<style lang="scss" scoped>
	.wrap {
			padding: 24rpx;
		}
	.u-row {
			margin: 40rpx 0;
		}
	.red {
		color: #fa3534;
		}

</style>