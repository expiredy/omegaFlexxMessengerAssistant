<template>
    <div>
        <div class="info-div-block">
            <h1>Welcome to my domain</h1>
            <h2>Here we got a little test to get which mode of our assistent
                will fit you the most
            </h2>
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