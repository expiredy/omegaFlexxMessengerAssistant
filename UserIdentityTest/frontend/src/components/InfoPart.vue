<template>
    <div>
        <div class="info-div-block">
            <h1>Welcome to my domain</h1>
            <h2>Here we got a little test to get which mode of our assistent
                will fit you the most
            </h2>
        </div>
        <div class="task-block">
            <h2>Here is we will ask you a few questions and you need to answer
                 "How relatable is for you? in range from -1 (not relatable) to 1 (relatable)
                 and 0 is something like: "I don't know..."</h2>
        </div>
    </div>
</template>

<script>
    export default {
    name: 'Information'
    }
</script>

<style>
    .info-part{
        background: rgb(59, 59, 59);
        border-block-color: black;
        border-block-width: 15px;
    }

    .info-part:hover{
        box-shadow: saddlebrown;
    }

    h1{
        height: 55px;
        color:rgb(177, 177, 177);
    }

    h2{
        color: rgb(160, 160, 160);
    }


</style>