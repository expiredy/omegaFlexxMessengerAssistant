<template>
	<div class="questionnaire">
    	<div v-for="questionItem in questionsArray" v-bind:key="questionItem.id">
			<h2>{{questionItem.question}}</h2>
			<div style="height: 50px;">
				<div v-for="answerIndex in questionItem .AnswerWeightsArray" :key="answerIndex" class="rb-tab" :data-value="answerIndex.lenght">
					<input type="radio" @click="answerVariableHolder (questionItem.buttonName, answerIndex)"
					 :name="questionItem.buttonName">
					<label>{{ answerIndex }}</label> 
					<!-- <input @click="answerVariableHolder (questionItem.buttonName, answerIndex)"
					 :name="questionItem.buttonName" type="radio" class="open">
						<label class="overlay">
							<div class="circle"></div> 
							<span class=text>{{answrerIndex}}</span>  
						</label> -->
				</div>
			</div>
		</div>
		<div class="confirmation-field"  @click="sendDataToAnalyzer">
			<span class="confirming-button-span">
				<a></a>
			</span>
		</div>
	</div>	
</template>

<script>
export default {
	name: 'Questionnaire',
	
	props: {
	questions: Array,
	marksForAnswer: Array,
	},
	data: function(){return{
		defaultQuestionsAnswersArray: [-1, 0, 1],

		questionsArray: [
			{question: 'Are you dumb?',
			 buttonName: "answer1",
			 AnswerWeightsArray: defaultQuestionsAnswersArray},
			{question: 'Wanna see my backugan cards collection?',
			 buttonName: "answer2",
			 AnswerWeightsArray: defaultQuestionsAnswersArray},
			{question: 'Frontend?',
			 buttonName: "answer3",
			 AnswerWeightsArray: defaultQuestionsAnswersArray}
		],
		CallbackAnswerWeights: {}
		}},
	methods: {
		answerVariableHolder: function(answerName, weight){
			if (!Object.prototype.hasOwnProperty.call(this.CallbackAnswerWeights, answerName)){
				this.CallbackAnswerWeights[answerName] = weight;}
		},

		sendDataToAnalyzer: function(){
			if (this.questionsArray.length == Object.keys(this.CallbackAnswerWeights).length){
				window.location.replace("http://stackoverflow.com");
			}
			else{
				alert("First at first you need to answer all questions");
			}
		}
	},
}
</script>

<style>
	@import './../main.css';
	@import './stylesheets/radiobutton_style.css';
	@import './stylesheets/confirmationButtonStyle.css';
</style>